from django.http import HttpResponse
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings

from .models import Order, OrderLineItem
from services.models import Service

import json
import time


class StripeWH_Handler:
    """ Handle Stripe Hooks """

    # The init method of the class is a setup method
    # that's called every time an instance of the
    # class is created.
    def __init__(self, request):
        self.request = request

    def _send_confirmation_email(self, order):
        """ Send user a confirmation email """

        cust_email = order.email
        subject = render_to_string(
            'checkout/confirmation_emails/confirmation_email_subject.txt',
            {'order': order})
        body = render_to_string(
            'checkout/confirmation_emails/confirmation_email_body.txt',
            {'order': order, 'contact_email': settings.DEFAULT_FROM_EMAIL})

        send_mail(
            subject,
            body,
            settings.DEFAULT_FROM_EMAIL,
            [cust_email]
        )

    def handle_event(self, event):
        """ Handle a generic/unknown unexpected webhook event """

        return HttpResponse(
            content=f'Unhandled webhook recieved: {event["type"]}',
            status=200)

    def handle_payment_intent_succeeded(self, event):
        """ Handle the payment_intent.succeeded webhook from Stripe """

        # Create an order in case the form isn't submitted
        intent = event.data.object
        pid = intent.id
        order = intent.metadata.order

        billing_details = intent.charges.data[0].billing_details
        grand_total = round(intent.charges.data[0].amount / 100, 2)

        order_exists = False

        # Create a delay incase the view is slow
        attempt = 1
        while attempt <= 5:
            try:
                order = Order.objects.get(
                    # Use iexact to get an exact match but case-insensitive
                    full_name__iexact=billing_details.name,
                    user_profile=profile,
                    email__iexact=billing_details.email,
                    phone_number__iexact=billing_details.phone,
                    country__iexact=billing_details.address.country,
                    postcode__iexact=billing_details.address.postal_code,
                    town_or_city__iexact=billing_details.address.city,
                    street_address__iexact=billing_details.address.line1,
                    apartment_no__iexact=billing_details.address.line2,
                    county__iexact=billing_details.address.state,
                    grand_total=grand_total,
                    original_order_contents=order,
                    stripe_pid=pid,
                )
                order_exists = True
                # If the order is found, break out of the loop
                break
            # If the order isn't found then increment attempt and
            # use Python's time module to sleep for one second
            except Order.DoesNotExist:
                attempt += 1
                time.sleep(1)

        if order_exists:
            # if we found the order in the database because it was already
            # created in the form, send the confirmation email before
            # returning that response to stripe
            self._send_confirmation_email(order)
            return HttpResponse(
                content=f'Webhook recieved: {event["type"]} | SUCCESS: Verified order already in database',
                status=200)
        else:
            order = None
            try:
                order = Order.objects.create(
                    full_name=billing_details.name,
                    email=billing_details.email,
                    phone_number=billing_details.phone,
                    country=billing_details.address.country,
                    postcode=billing_details.address.postal_code,
                    town_or_city=billing_details.address.city,
                    street_address1=billing_details.address.line1,
                    apartment_no=billing_details.address.line2,
                    county=billing_details.address.state,
                    grand_total=grand_total,
                    original_order_contents=order,
                    stripe_pid=pid,
                )

                for data in json.loads(order).items():
                    service = Service.objects.get(pk=data['service_id'])
                    order_line_item = OrderLineItem(
                        order=order,
                        service=service,
                        quantity=data['quantity'],
                    )
                    order_line_item.save()
            except Exception as e:
                if order:
                    order.delete()
                # Return 500 server response to stripe which will cause stripe
                # to automatically try the webhook again later
                return HttpResponse(
                    content=f'Webhook recieved: {event["type"]} | ERROR: {e}',
                    status=500)

        self._send_confirmation_email(order)
        return HttpResponse(
            content=f'Webhook recieved: {event["type"]} | SUCCESS: Created order in webhook',
            status=200)

    def handle_payment_intent_payment_failed(self, event):
        """ Handle the payment_intent.payment_failed webhook from Stripe """
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200)

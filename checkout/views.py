from checkout.contexts import order_contents
from django.shortcuts import redirect, render, reverse, get_object_or_404
from django.contrib import messages
from django.conf import settings
from django.contrib.auth.decorators import login_required

from .models import Order, OrderLineItem
from profiles.models import UserProfile
from services.models import Service
from checkout.forms import OrderForm

import stripe
import json


def checkout(request, service_id):
    """ A view to add a service to checkout and
    render the content of the checkout page """

    # Grab service object
    service = get_object_or_404(Service, pk=service_id)

    # Create new session for order
    order = request.session.get('order', {})

    # Get delivery type (fast or standard)
    if 'delivery' in request.POST:
        delivery = request.POST.get('delivery')
    else:
        if 'order' in request.session:
            if order['service_id'] == service_id:
                delivery = order['delivery']
            else:
                delivery = 0
        else:
            delivery = 0

    delivery = float(delivery)

    # Get service package type
    if 'package' in request.POST:
        package = request.POST.get('package', 'basic')
    else:
        if 'order' in request.session:
            if order['service_id'] == service_id:
                package = order['package']
            else:
                package = request.POST.get('package', 'basic')

    # Get order quantity
    if 'quantity' in request.POST:
        quantity = request.POST.get('quantity', 1)
    else:
        if 'order' in request.session:
            if order['service_id'] == service_id:
                quantity = order['quantity']
            else:
                quantity = 1
        else:
            quantity = 1

    if request.user.is_authenticated:
        buyer = request.user.email
    else:
        buyer = None

    # Add form values to order session
    order['service_id'] = service_id
    order['buyer'] = buyer
    order['delivery'] = delivery
    order['package'] = package
    order['quantity'] = quantity

    # Update order session
    request.session['order'] = order

    # Determine the chosen package
    if package == 'basic':
        chosen_package = service.basicpackage
    elif package == 'standard':
        chosen_package = service.standardpackage
    elif package == 'premium':
        chosen_package = service.premium

    # Calculate subtotal and grand total
    starting_price = chosen_package.price

    delivery_price = [
        0 if delivery == 0 else chosen_package.fast_delivery_price]

    quantity_total = starting_price * int(quantity)

    subtotal = quantity_total + delivery_price[0]
    service_fee = (subtotal / 10) / 2

    grand_total = subtotal + service_fee

    template = 'checkout/checkout.html',
    context = {
        'service': service,
        'package': chosen_package,
        'delivery': delivery,
        'subtotal': subtotal,
        'service_fee': service_fee,
        'quantity': quantity,
        'quantity_total': quantity_total,
        'grand_total': grand_total,
    }
    return render(request, template, context)


@login_required
def checkout_payment(request, service_id):
    """ A view to process payment for an order """

    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    current_order = order_contents(request)
    service = get_object_or_404(Service, pk=service_id)
    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        order = request.session.get('order', {})

        form_data = {
            'full_name': request.POST.get('full_name'),
            'email': request.POST.get('email'),
            'company_name': request.POST.get('company_name'),
            'street_address': request.POST.get('street_address'),
            'apartment_no': request.POST.get('apartment_no'),
            'town_or_city': request.POST.get('town_or_city'),
            'country': request.POST.get('country'),
            'county': request.POST.get('county'),
            'postcode': request.POST.get('postcode'),
            'phone_number': request.POST.get('phone_number'),
        }
        form = OrderForm(form_data)
        if form.is_valid():
            user_order = form.save(commit=False)
            user_order.profile = profile
            user_order.save()

            pid = request.POST.get('client_secret').split('_secret')[0]
            user_order.stripe_pid = pid
            user_order.original_order_contents = json.dumps(order)
            user_order.save()

            package = current_order['package']

            order_line_item = OrderLineItem(
                order=user_order,
                service=service,
                package=package,
                service_price=package.price,
                quantity=current_order['quantity'],
                delivery_cost=current_order['delivery'],
            )
            order_line_item.save()

            request.session['save_info'] = 'save_info' in request.POST
            return redirect(reverse(
                'checkout_success', args=[user_order.order_number]))
        else:
            messages.error(request, 'There was an error with your form. \
                Please double check your information.')
    else:
        order = request.session.get('order', {})
        if not order:
            messages.error(
                request, "You must select a service before you a payment")
            return redirect(reverse('service_details', args=(service_id)))

        total = current_order['grand_total']
        stripe_total = round(total * 100)
        stripe.api_key = stripe_secret_key
        intent = stripe.PaymentIntent.create(
            amount=stripe_total,
            currency=settings.STRIPE_CURRENCY,
        )

        form = OrderForm()

    if not stripe_public_key:
        messages.warning(request, 'Stripe public key is missing. \
            Did you forget to set it in your environment?')

    template = 'checkout/checkout-payment.html'
    context = {
        'current_order': current_order,
        'service': service,
        'form': form,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
    }
    return render(request, template, context)


def checkout_success(request, order_number):
    """ A view to handle successful checkouts """

    order = get_object_or_404(Order, order_number=order_number)

    template = 'checkout/checkout-success.html'
    context = {
        'order': order,
    }

    return render(request, template, context)

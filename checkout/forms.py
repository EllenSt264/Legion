from django.http import request
from checkout.models import Order
from django import forms


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        exclude = (
            'profile', 'order_number', 'stripe_pid', 'date',
            'original_order_contents', 'delivery_cost',
            'service_fee', 'grand_total', 'order_subtotal',
        )

        labels = {
            'full_name': 'Full Name *',
            'email': 'Email Address *',
            'company_name': 'Company Name',
            'street_address': 'Street Address *',
            'apartment_no': 'Apartment, Suite etc.',
            'town_or_city': 'Town or City *',
            'country': '',
            'county': 'County',
            'postcode': 'Postal Code *',
            'phone_number': 'Phone Number *'
        }

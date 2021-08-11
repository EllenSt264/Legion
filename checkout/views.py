from django.shortcuts import redirect, render, reverse, get_object_or_404
from django.contrib import messages
from django.conf import settings
from django.contrib.auth.decorators import login_required

from services.models import Service


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

    service = get_object_or_404(Service, pk=service_id)

    if 'order' in request.session:
        order = request.session.get('order')
        print(order)
        print(request.user.email)
        if order['service_id'] is not service_id:
            return render(request, '404.html')
        if order['buyer'] != request.user.email:
            return render(request, '404.html')
    else:
        return redirect(reverse('checkout', args=(service_id,)))

    delivery = order['delivery']
    package = order['package']
    quantity = order['quantity']

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

    template = 'checkout/checkout-payment.html'
    context = {
        'service': service,
        'package': chosen_package,
        'delivery': delivery,
        'subtotal': subtotal,
        'service_fee': service_fee,
        'quantity': quantity,
        'quantity_total': quantity_total,
        'grand_total': grand_total,
        'stripe_public_key': stripe_public_key,
        'client_secret': stripe_secret_key,
    }
    return render(request, template, context)

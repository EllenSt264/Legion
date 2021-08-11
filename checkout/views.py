from django.shortcuts import redirect, render, reverse, get_object_or_404
from django.contrib import messages

from services.models import Service


def checkout(request, service_id):
    """ A view to add a service to checkout and
    render the content of the checkout page """

    service = get_object_or_404(Service, pk=service_id)

    order = request.session.get('order', {})

    delivery = request.POST.get('delivery', 0)
    package = request.POST.get('package', 'basic')

    if 'quantity' in request.POST:
        quantity = request.POST.get('quantity', None)
    else:
        quantity = 1

    order['service_id'] = service_id
    order['delivery'] = delivery
    order['package'] = package
    order['quantity'] = quantity

    request.session['order'] = order

    if package == 'basic':
        chosen_package = service.basicpackage
    elif package == 'standard':
        chosen_package = service.standardpackage
    elif package == 'premium':
        chosen_package = service.premium

    starting_price = chosen_package.price
    if delivery != 0:
        delivery_price = chosen_package.fast_delivery_price
    else:
        delivery_price = 0

    quantity_total = starting_price * int(quantity)

    subtotal = quantity_total + delivery_price
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

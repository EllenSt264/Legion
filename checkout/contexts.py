from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404

from services.models import Service


def order_contents(request):
    order_details = []

    order = request.session.get('order', {})

    if 'order' in request.session:
        service_id = order['service_id']
        delivery = order['delivery']
        package = order['package']
        quantity = order['quantity']

        service = get_object_or_404(Service, pk=service_id)

        order_details.append({
            'service_id': service_id,
            'service': service,
        })

        if package == 'basic':
            chosen_package = service.basicpackage
        elif package == 'standard':
            chosen_package = service.standardpackage
        elif package == 'premium':
            chosen_package = service.premium

        delivery_time = chosen_package.delivery_time

        total = chosen_package.price * int(quantity)
        subtotal = int(total) + int(delivery)
        service_fee = (subtotal / 10) / 2
        grand_total = subtotal + service_fee

        context = {
            'order_details': order_details,
            'package': chosen_package,
            'delivery': float(delivery),
            'delivery_time': delivery_time,
            'quantity': int(quantity),
            'total': float(total),
            'subtotal': float(subtotal),
            'service_fee': float(service_fee),
            'grand_total': float(grand_total),
        }
    else:
        context = {'order_details': order_details}
    return context

from django.contrib import admin
from .models import Order, OrderLineItem


class OrderLineItemAdminInline(admin.StackedInline):
    model = OrderLineItem
    extra = 0


class OrderAdmin(admin.ModelAdmin):
    list_display = (
        'order_number',
        'date',
        'full_name',
        'order_total',
        'delivery_cost',
        'grand_total'
    )

    inline_type = 'tabular'
    inlines = []
    inlines = (OrderLineItemAdminInline,)

    ordering = ('-date',)


admin.site.register(Order, OrderAdmin)

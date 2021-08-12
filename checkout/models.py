import uuid

from django.db import models
from django.db.models import Sum

from django_countries.fields import CountryField

from services.models import BasicPackage, Service
from profiles.models import UserProfile


class Order(models.Model):
    order_number = models.CharField(max_length=32, null=False, editable=False)

    profile = models.ForeignKey(
        UserProfile,
        on_delete=models.SET_NULL,
        related_name='orders',
        null=True,
        blank=True,
    )
    full_name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    company_name = models.CharField(max_length=50, null=True, blank=True)
    street_address = models.CharField(max_length=80, null=False, blank=False)
    apartment_no = models.CharField(max_length=80, null=True, blank=True)
    town_or_city = models.CharField(max_length=40, null=False, blank=False)
    country = CountryField(blank_label='Country *', null=False, blank=False)
    county = models.CharField(max_length=80, null=True, blank=True)
    postcode = models.CharField(max_length=20, null=True, blank=True)
    phone_number = models.CharField(max_length=20, null=False, blank=False)
    original_order_contents = models.TextField(null=False, blank=False, default='')

    delivery_cost = models.DecimalField(
        max_digits=6, decimal_places=2, null=False, default=0)
    order_total = models.DecimalField(
        max_digits=10, decimal_places=2, null=False, default=0)
    grand_total = models.DecimalField(
        max_digits=10, decimal_places=2, null=False, default=0)

    date = models.DateTimeField(auto_now_add=True)
    stripe_pid = models.CharField(
        max_length=254,
        null=False,
        blank=False,
        default='',
    )

    def _generate_order_number(self):
        """ Generate a random, unique order number using UUID  """

        return uuid.uuid4().hex.upper()

    def save(self, *args, **kwargs):
        """ Override original save method to set order number """

        if not self.order_number:
            self.order_number = self._generate_order_number()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.order_number


class OrderLineItem(models.Model):
    order = models.ForeignKey(Order, null=False, blank=False, on_delete=models.CASCADE, related_name='lineitems')
    service = models.ForeignKey(Service, null=False, blank=False, on_delete=models.CASCADE)
    package = models.ForeignKey(BasicPackage, null=False, blank=False, on_delete=models.CASCADE, related_name='package')

    quantity = models.IntegerField(null=True, blank=True, default=0)
    delivery_cost = models.DecimalField(max_digits=6, decimal_places=2, null=False, blank=False)
    service_price = models.DecimalField(max_digits=6, decimal_places=2, null=False, blank=False, editable=False)
    subtotal = models.DecimalField(max_digits=6, decimal_places=2, null=False, blank=False, editable=False)
    service_fee = models.DecimalField(max_digits=6, decimal_places=2, null=False, blank=False, editable=False)
    grand_total = models.DecimalField(max_digits=6, decimal_places=2, null=False, blank=False, editable=False)

    # Set the line-item total field by overriding its save method
    def save(self, *args, **kwargs):
        """ Override original save method to set order number """

        self.subtotal = (float(self.service_price) * self.quantity) + self.delivery_cost

        self.service_fee = (self.subtotal / 10) / 2
        self.grand_total = self.subtotal + self.service_fee

        super().save(*args, **kwargs)

    def __str__(self):
        return self.order.order_number

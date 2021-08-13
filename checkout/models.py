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

    def update_total(self):
        """ Update total price """

        self.grand_total = self.lineitem.aggregate(
            Sum('lineitem_total'), self.lineitem.service_fee)
        self.save()

    def save(self, *args, **kwargs):
        """ Override original save method to set order number """

        if not self.order_number:
            self.order_number = self._generate_order_number()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.order_number


class OrderLineItem(models.Model):
    order = models.ForeignKey(Order, null=False, blank=False, on_delete=models.CASCADE, related_name='lineitem')
    service = models.ForeignKey(Service, null=False, blank=False, on_delete=models.CASCADE)
    package = models.ForeignKey(BasicPackage, null=False, blank=False, on_delete=models.CASCADE, related_name='package')
    quantity = models.IntegerField(null=True, blank=True, default=0)
    delivery_cost = models.DecimalField(max_digits=6, decimal_places=2, null=False, blank=False, default=0)
    service_fee = models.DecimalField(max_digits=6, decimal_places=2, null=False, blank=False, default=0)
    lineitem_total = models.DecimalField(max_digits=6, decimal_places=2, null=False, blank=False, editable=False)

    def save(self, *args, **kwargs):
        """ Override original save method to set order number """

        self.lineitem_total = self.package.price * self.quantity

    def __str__(self):
        return self.order.order_number

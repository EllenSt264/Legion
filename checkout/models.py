from django.db import models
from django.http import request

from django_countries.fields import CountryField

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

    date = models.DateTimeField(auto_now_add=True)
    stripe_pid = models.CharField(
        max_length=254,
        null=False,
        blank=False,
        default='',
    )

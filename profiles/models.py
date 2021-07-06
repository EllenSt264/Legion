from django.conf import settings
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from django_countries.fields import CountryField
User = settings.AUTH_USER_MODEL


class UserProfile(models.Model):
    """ A class model for creating a user profile, which
    shall extend the custom user model defined in the accounts app """

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=True,
    )

    title = models.CharField(max_length=50, null=True, blank=True, default='')
    overview = models.TextField(null=True, blank=True, default='')
    image = models.ImageField(null=True, blank=True)

    is_recruiter = models.BooleanField(default=False)
    is_creator = models.BooleanField(default=False)

    def __str__(self):
        return self.user.email


class Recruiter(models.Model):
    """ A class model for the recruiter user type """

    company_name = models.CharField(max_length=70, null=False, blank=False)

    town_or_city = models.CharField(max_length=70, null=False, blank=False)
    postcode = models.CharField(max_length=70, null=False, blank=False)
    country = CountryField(blank_label='Select Country', null=True, blank=True)


@receiver(post_save, sender=User)
def update_profile_signal(sender, instance, created, **kwargs):
    """ A signal to update or create the user profile """
    user = instance
    if created:
        profile = UserProfile(user=user)
        profile.save()

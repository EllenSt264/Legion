from django.db import models
from django.contrib.auth import get_user_model
from django.http import request


User = get_user_model()


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.email


class UserRecruiter(models.Model):
    """ A user profile model for users who will use the site as recruiters """

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    is_client = models.BooleanField(default=True)
    is_recruiter = models.BooleanField(default=False)
    company_name = models.CharField(max_length=80, null=True, blank=True)

    def __str__(self):
        return self.user.email

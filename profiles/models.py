from django.conf import settings
from django.db import models
from django.db.models.signals import post_save
from django.utils.translation import gettext_lazy as _
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

    class Meta:
        verbose_name_plural = 'Profiles'

    profile = models.OneToOneField(
        UserProfile,
        on_delete=models.CASCADE,
        related_name='profile',
        primary_key=True,
        default='',
    )

    company_name = models.CharField(max_length=70, null=False, blank=False)
    town_or_city = models.CharField(max_length=70, null=False, blank=False)
    postcode = models.CharField(max_length=70, null=False, blank=False)
    country = CountryField(blank_label='Select Country', null=True, blank=True)

    def __str__(self):
        return self.profile.user.email


class Creator(models.Model):
    """ A class model for the creator user type """

    profile = models.OneToOneField(
        UserProfile,
        on_delete=models.CASCADE,
        related_name='user_profile',
        primary_key=True,
        default='',
    )

    town_or_city = models.CharField(max_length=70, null=False, blank=False)
    postcode = models.CharField(max_length=70, null=False, blank=False)
    country = CountryField(blank_label='Select Country', null=False, blank=False)

    def __str__(self):
        return self.profile.user.email


class Category(models.Model):
    DEV = 'DE'
    CREATIVE = 'CR'
    WRITING = 'WR'
    TRANSLATION = 'TR'
    CATEGORY_CHOICES = [
        ('Web, Mobile & Software Dev', (
                ('DESKTOP', 'Desktop Software Development'),
                ('MOBILE', 'Mobile Development'),
                ('GAME', 'Game Development'),
                ('OTHER', 'Other Software Development'),
                ('TESTING', 'Testing'),
                ('UX', 'Web UX & Mobile Design'),
                ('WEB', 'Web Development'),
            )),
        ('Design & Creative', (
                ('ART', 'Art & Illustration'),
                ('AUDIO', 'Audio & Music Production'),
                ('VIDEO', 'Video & Animation'),
                ('DESIGN', 'Graphic, Editorial & Presentation Design'),
                ('ARTS', 'Performing Arts'),
                ('PHOTO', 'Photography'),
                ('BRANDING', 'Branding & Logo Design'),
                ('GAMING', 'Gaming AR/VR'),
            )),
        ('Writing', (
                ('CONTENT', 'Content & Copyright'),
                ('CREATIVE', 'Creative'),
                ('EDITING', 'Editing & Proofreading'),
                ('RESUMES', 'Resumes & Cover Letters'),
                ('TECHNICAL', 'Technical Writing'),
            )),
        ('Translation', (
                ('GENERAL', 'General'),
                ('LEGAL', 'Legal'),
                ('MEDICAL', 'Medical'),
                ('TECHNICAL', 'Technical'),
            )),
    ]

    profile = models.OneToOneField(
        UserProfile,
        on_delete=models.CASCADE,
        related_name='profile_cat',
        null=True,
        blank=True,
    )

    category_name = models.CharField(
        max_length=70,
        choices=CATEGORY_CHOICES,
        default=DEV,
        null=False,
        blank=False,
    )


class CreatorWork(models.Model):
    profile = models.OneToOneField(
        UserProfile,
        on_delete=models.CASCADE,
        related_name='profile_work',
        null=True,
        blank=True,
    )

    skills = models.CharField(max_length=70, null=True, blank=True)

    class Expertise(models.IntegerChoices):
        ENTRY = 1
        INTERMEDIATE = 2
        EXPERT = 3

    expertise_level = models.IntegerField(
        choices=Expertise.choices,
        default=Expertise.ENTRY,
    )

    def __str__(self):
        fname = self.profile.user.first_name.title()
        lname = self.profile.user.last_name.title()
        return f'{fname} {lname}'


class Education(models.Model):
    profile = models.OneToOneField(
        UserProfile,
        on_delete=models.CASCADE,
        related_name='profile_ed',
        null=True,
        blank=True,
    )

    institution_name = models.CharField(max_length=70, null=True, blank=True)
    area_of_study = models.CharField(max_length=70, null=True, blank=True)
    qualification = models.CharField(max_length=70, null=True, blank=True)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        fname = self.profile.user.first_name.title()
        lname = self.profile.user.last_name.title()
        return f'{fname} {lname}'


class WorkExperience(models.Model):
    profile = models.OneToOneField(
        UserProfile,
        on_delete=models.CASCADE,
        related_name='profile_workex',
        null=True,
        blank=True,
    )

    company_name = models.CharField(max_length=70, null=True, blank=True)
    work_town_or_city = models.CharField(max_length=70, null=True, blank=True)
    work_country = CountryField(blank_label='Country', null=True, blank=True)
    job_title = models.CharField(max_length=70, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    currently_working_here = models.BooleanField(default=False, null=True, blank=True)

    def __str__(self):
        fname = self.profile.user.first_name.title()
        lname = self.profile.user.last_name.title()
        return f'{fname} {lname}'


class Languages(models.Model):
    profile = models.OneToOneField(
        UserProfile,
        on_delete=models.CASCADE,
        related_name='profile_lang',
        null=True,
        blank=True,
    )

    class Proficiency(models.IntegerChoices):
        BASIC = 1
        CONVERSATIONAL = 2
        FLUENT = 3
        NATIVE_BILINGUAL = 4

    english_proficiency = models.IntegerField(
        choices=Proficiency.choices,
        default=Proficiency.FLUENT,
        null=False,
        blank=False,
    )

    language = models.CharField(max_length=70, null=True, blank=True)
    language_proficiency = models.IntegerField(
        choices=Proficiency.choices,
        default=Proficiency.FLUENT,
        null=True,
        blank=True,
    )

    def __str__(self):
        fname = self.profile.user.first_name.title()
        lname = self.profile.user.last_name.title()
        return f'{fname} {lname}'


def create_profile(sender, instance, created, *args, **kwargs):
    # ignore if this is an existing User
    if not created:
        return
    UserProfile.objects.create(user=instance)


post_save.connect(create_profile, sender=User)

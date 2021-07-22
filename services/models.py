from django.db import models
from django.conf import settings


User = settings.AUTH_USER_MODEL


class FreelanceService(models.Model):
    """ A class model for users to create and
    add a service to the application """

    class Meta:
        verbose_name_plural = 'Freelance Services'

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )

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

    category_name = models.CharField(
        max_length=80,
        choices=CATEGORY_CHOICES,
        null=False,
        blank=False,
    )

    service_headline = models.CharField(max_length=50, null=False, blank=False)
    service_description = models.TextField(null=False, blank=False)
    service_search_tags = models.CharField(
        max_length=120,
        null=True,
        blank=True
    )
    service_image = models.ImageField(null=True, blank=True)

    faq_question = models.CharField(max_length=120, null=True, blank=True)
    faq_answer = models.TextField(null=True, blank=True)

    class DeliveryTimes(models.IntegerChoices):
        ONE_DAY = 1
        TWO_DAY = 2
        THREE_DAY = 3
        FOUR_DAY = 4
        FIVE_DAY = 5
        SIX_DAY = 6
        SEVEN_DAY = 7
        TWELVE_DAY = 12
        TWO_WEEK = 14
        THREE_WEEK = 21
        ONE_MONTH = 30

    class NumberRevisions(models.IntegerChoices):
        ZERO = 0
        ONE = 1
        TWO = 2
        THREE = 3
        FOUR = 4
        FIVE = 5
        SIX = 6
        SEVEN = 7
        EIGHT = 8

    enable_all_packages = models.BooleanField(default=True)

    basic_package_title = models.CharField(
        max_length=50,
        null=False,
        blank=False
    )
    basic_delivery_time = models.IntegerField(choices=DeliveryTimes.choices)
    basic_revisions = models.IntegerField(choices=NumberRevisions.choices)
    basic_details = models.TextField()
    basic_price = models.DecimalField(max_digits=6, decimal_places=2)

    standard_package_title = models.CharField(
        max_length=50,
        null=True,
        blank=True
    )
    standard_delivery_time = models.IntegerField(
        choices=DeliveryTimes.choices,
        null=True,
        blank=True
    )
    standard_revisions = models.IntegerField(
        choices=NumberRevisions.choices,
        null=True,
        blank=True
    )
    standard_details = models.TextField(null=True, blank=True)
    standard_price = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        null=True,
        blank=True
    )

    premium_package_title = models.CharField(
        max_length=50,
        null=True,
        blank=True
    )
    premium_delivery_time = models.IntegerField(
        choices=DeliveryTimes.choices,
        null=True,
        blank=True
    )
    premium_revisions = models.IntegerField(
        choices=NumberRevisions.choices,
        null=True,
        blank=True
    )
    premium_details = models.TextField(null=True, blank=True)
    premium_price = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        null=True,
        blank=True
    )

    def __str__(self):
        return self.category_name

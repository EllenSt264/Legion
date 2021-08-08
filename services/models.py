from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL


class Category(models.Model):
    """ A model class for services' category fixtures """

    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class SubCategory(models.Model):
    """ A model class for services' subcategory fixtures """

    class Meta:
        verbose_name_plural = 'SubCategories'

    category = models.ForeignKey(
        'Category',
        null=True,
        blank=True,
        on_delete=models.SET_NULL
    )
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Service(models.Model):
    """ A class model for users to create and add services """

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )

    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
    )

    subcategory = models.ForeignKey(
        SubCategory,
        on_delete=models.CASCADE,
    )

    headline = models.CharField(max_length=90, null=False, blank=False)
    description = models.TextField(null=False, blank=False)
    search_tags = models.CharField(
        max_length=120,
        null=True,
        blank=True
    )
    images = models.ImageField(null=True, blank=True)

    faq_question_1 = models.CharField(max_length=120, null=True, blank=True)
    faq_answer_1 = models.TextField(null=True, blank=True)

    faq_question_2 = models.CharField(max_length=120, null=True, blank=True)
    faq_answer_2 = models.TextField(null=True, blank=True)

    faq_question_3 = models.CharField(max_length=120, null=True, blank=True)
    faq_answer_3 = models.TextField(null=True, blank=True)

    faq_question_4 = models.CharField(max_length=120, null=True, blank=True)
    faq_answer_4 = models.TextField(null=True, blank=True)

    include_client_requirements = models.BooleanField(default=False)
    requirements_same_for_all = models.BooleanField(default=True)

    shipping_required = models.BooleanField(default=False)

    def __str__(self):
        return self.headline


class BasicPackage(models.Model):
    """ A model for creators to specify
    the package details, requirements and price """

    service = models.OneToOneField(
        Service,
        on_delete=models.CASCADE,
        primary_key=True,
    )

    enable_all_packages = models.BooleanField(default=True)

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

    package_title = models.CharField(
        max_length=90,
        null=False,
        blank=False
    )
    package_description = models.TextField(null=False, blank=False)
    client_requirements = models.TextField(null=True, blank=True)

    delivery_time = models.IntegerField(choices=DeliveryTimes.choices)
    revisions = models.IntegerField(choices=NumberRevisions.choices)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    fast_delivery_time = models.IntegerField(
        choices=DeliveryTimes.choices,
        null=True,
        blank=True,
    )
    fast_delivery_price = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        null=True,
        blank=True,
    )
    reference_images = models.ImageField(null=True, blank=True)


class StandardPackage(models.Model):
    """ A model for creators to specify
    the package details, requirements and price """

    service = models.OneToOneField(
        Service,
        on_delete=models.CASCADE,
        primary_key=True,
    )

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

    standard_package_title = models.CharField(
        max_length=90,
        null=True,
        blank=True
    )
    standard_package_description = models.TextField(null=True, blank=True)
    standard_client_requirements = models.TextField(null=True, blank=True)

    standard_delivery_time = models.IntegerField(
        choices=DeliveryTimes.choices,
        null=True,
        blank=True,
    )
    standard_revisions = models.IntegerField(
        choices=NumberRevisions.choices,
        null=True,
        blank=True,
    )
    standard_price = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        null=True,
        blank=True,
    )

    standard_fast_delivery_time = models.IntegerField(
        choices=DeliveryTimes.choices,
        null=True,
        blank=True,
    )
    standard_fast_delivery_price = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        null=True,
        blank=True,
    )
    standard_reference_images = models.ImageField(null=True, blank=True)


class PremiumPackage(models.Model):
    """ A model for creators to specify
    the package details, requirements and price """

    service = models.OneToOneField(
        Service,
        on_delete=models.CASCADE,
        primary_key=True,
    )

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

    premium_package_title = models.CharField(
        max_length=90,
        null=True,
        blank=True
    )
    premium_package_description = models.TextField(null=True, blank=True)
    premium_client_requirements = models.TextField(null=True, blank=True)

    premium_delivery_time = models.IntegerField(
        choices=DeliveryTimes.choices,
        null=True,
        blank=True,
    )
    premium_revisions = models.IntegerField(
        choices=NumberRevisions.choices,
        null=True,
        blank=True,
    )
    premium_price = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        null=True,
        blank=True,
    )

    premium_fast_delivery_time = models.IntegerField(
        choices=DeliveryTimes.choices,
        null=True,
        blank=True,
    )
    premium_fast_delivery_price = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        null=True,
        blank=True,
    )
    premium_reference_images = models.ImageField(null=True, blank=True)


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
                ('TECH', 'Technical'),
            )),
    ]

    category_name = models.CharField(
        max_length=80,
        choices=CATEGORY_CHOICES,
        null=False,
        blank=False,
    )

    service_headline = models.CharField(max_length=90, null=False, blank=False)
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
        max_length=90,
        null=False,
        blank=False
    )
    basic_delivery_time = models.IntegerField(choices=DeliveryTimes.choices)
    basic_revisions = models.IntegerField(choices=NumberRevisions.choices)
    basic_details = models.TextField()
    basic_price = models.DecimalField(max_digits=6, decimal_places=2)

    standard_package_title = models.CharField(
        max_length=90,
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
        max_length=90,
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

from django.db import models
from django.utils.timezone import now
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager


class UserManager(BaseUserManager):
    def create_user(
            self, first_name, last_name, email,
            date_of_birth, phone_number, password=None):
        """ Creates and saves a User with a given email, DOB and password """

        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            first_name=first_name,
            last_name=last_name,
            email=self.normalize_email(email),
            date_of_birth=date_of_birth,
            phone_number=phone_number,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(
            self, first_name, last_name, email,
            date_of_birth, phone_number, password=None):
        """ Creates and saves a Superuser with a given email,
        DOB and password """

        user = self.create_user(
            first_name,
            last_name,
            email,
            password=password,
            date_of_birth=date_of_birth,
            phone_number=phone_number,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    first_name = models.CharField(
        verbose_name='first name',
        max_length=35,
        blank=True,
        null=True,
    )
    last_name = models.CharField(
        verbose_name='last name',
        max_length=35,
        blank=True,
        null=True,
    )
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    date_of_birth = models.DateField(
        verbose_name='date of birth',
        default=now().strftime('%Y-%m-%d'),
    )
    phone_number = PhoneNumberField(
        verbose_name='phone number',
        blank=True,
        null=True,
    )
    is_creator = models.BooleanField(default=False)
    is_recruiter = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = [
        'first_name', 'last_name',
        'date_of_birth', 'phone_number']

    def __str__(self):
        return self.email

    def get_full_name(self):
        return f'{self.first_name} {self.last_name}'

    def get_short_name(self):
        return self.first_name

    def has_perm(self, perm, obj=None):
        """ Does the user have a specific permission? """
        return True

    def has_module_perms(self, app_label):
        """ Does the user have permissions to view the app 'app_label'? """
        return True

    @property
    def is_staff(self):
        """ Is the user a staff member? """
        # All admins are staff memebers
        return self.is_admin

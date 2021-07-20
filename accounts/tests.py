from django.contrib.auth import get_user_model
from django.http import HttpRequest
from django.test import TestCase
from .admin import UserCreationForm


class SignUpTest(TestCase):
    def test_create_user_model(self):
        """ Test sign up custom user model """

        User = get_user_model()
        user = User.objects.create(
            first_name='Jon',
            last_name='Smith',
            email='test@mail.com',
            date_of_birth='1998-01-01',
            phone_number='+441234567890',
            password='secret',
        )
        user.save()
        self.assertEqual(User.objects.count(), 1)

    def test_create_user_form(self):
        """ Test sign up form is valid """

        request = HttpRequest()
        request.POST = {
            'first_name': 'Jon',
            'last_name': 'Smith',
            'email': 'test@mail.com',
            'date_of_birth': '1998-01-01',
            'phone_number': '+441234567890',
            'password1': 'secret',
            'password2': 'secret',
        }
        form = UserCreationForm(request.POST)
        self.assertTrue(form.is_valid())
        form.save()

    def test_email_is_valid(self):
        """ Test if email validation works correctly """

        credentials = {
            'first_name': 'Jon',
            'last_name': 'Smith',
            'email': 'test',
            'date_of_birth': '1998-01-01',
            'phone_number': '+441234567890',
            'password': 'secret',
        }
        form = UserCreationForm(credentials)

        self.assertFalse(form.is_valid())
        self.assertIn('email', form.errors.keys())
        self.assertEqual(form.errors['email'][0], 'Enter a valid email address.')

    def test_age_requirement(self):
        """ The test should fail if
        the user is under 16 """

        credentials = {
            'first_name': 'Jon',
            'last_name': 'Smith',
            'email': 'test@mail.com',
            'date_of_birth': '2010-01-01',
            'phone_number': '+441234567890',
            'password': 'secret',
        }
        form = UserCreationForm(credentials)

        self.assertFalse(form.is_valid())
        self.assertIn('date_of_birth', form.errors.keys())
        self.assertEqual(form.errors['date_of_birth'][0], 'You must be at least 16 to register')

    def test_dob_is_valid(self):
        """ The test should fail if
        the DOB field is invalid """

        credentials = {
            'first_name': 'Jon',
            'last_name': 'Smith',
            'email': 'test@mail.com',
            'date_of_birth': '1998',
            'phone_number': '+441234567890',
            'password': 'secret',
        }
        form = UserCreationForm(credentials)

        self.assertFalse(form.is_valid())
        self.assertIn('date_of_birth', form.errors.keys())
        self.assertEqual(form.errors['date_of_birth'][0], '“1998” value has an invalid date format. It must be in YYYY-MM-DD format.')

    def test_phone_number_is_valid(self):
        """ The test should fail if the
        phone number field is invalid """

        credentials = {
            'first_name': 'Jon',
            'last_name': 'Smith',
            'email': 'test@mail.com',
            'date_of_birth': '1998-01-01',
            'phone_number': '1235',
            'password': 'secret',
        }
        form = UserCreationForm(credentials)

        self.assertFalse(form.is_valid())
        self.assertIn('phone_number', form.errors.keys())
        self.assertEqual(form.errors['phone_number'][0], 'Enter a valid phone number (e.g. +12125552368).')


class LogInTest(TestCase):
    def test_user_get_started_redirect(self):
        User = get_user_model()
        user = User.objects.create(
            first_name='Jon',
            last_name='Smith',
            email='test@mail.com',
            date_of_birth='1998-01-01',
            phone_number='+441234567890',
            password='secret',
        )
        user.save()

        self.client.login(email="test@mail.com", password="secret")
        response = self.client.get('/profile/get-started/', follow=True)

        self.assertRedirects(response, '/accounts/login/?next=/profile/get-started/')
        self.assertEqual(response.status_code, 200)

    def test_user_profile_redirect(self):
        User = get_user_model()
        user = User.objects.create(
            first_name='Jon',
            last_name='Smith',
            email='test@mail.com',
            date_of_birth='1998-01-01',
            phone_number='+441234567890',
            password='secret',
        )
        user.is_creator = True
        user.save()

        self.client.login(email="test@mail.com", password="secret")
        response = self.client.get('/profile/', follow=True)

        self.assertRedirects(response, '/accounts/login/?next=/profile/')
        self.assertEqual(response.status_code, 200)

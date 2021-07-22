from django.contrib.auth import get_user_model
from django.http import request
from django.test import TestCase

from .models import FreelanceService
from .forms import FreelanceServiceForm


class AddServiceTest(TestCase):
    def test_service_model(self):
        """ Test freelance service model """

        # Create user
        User = get_user_model()
        user = User.objects.create(
            first_name='Jon',
            last_name='Smith',
            email='test@mail.com',
            date_of_birth='1998-01-01',
            phone_number='+441234567890',
            password='secret',
        )

        # Test Service model
        service = FreelanceService.objects.create(
            user=user,
            category_name='WEB',
            service_headline='Test headline',
            service_search_tags='Hey,there',
            service_description='Testing the service description',
            enable_all_packages=False,
            faq_question='Can you work with Django?',
            faq_answer='Yes, I also do manual testing and document my findings.',
            basic_package_title='Here is the basic package in a few words',
            basic_delivery_time=1,
            basic_revisions=1,
            basic_details='Here are is additional information',
            basic_price=15,
            standard_package_title='Here is the standard package in a few words',
            standard_delivery_time=1,
            standard_revisions=1,
            standard_details='Here are is additional information',
            standard_price=15,
            premium_package_title='Here is the premium package in a few words',
            premium_delivery_time=1,
            premium_revisions=1,
            premium_details='Here are is additional information',
            premium_price=15,
            service_image='',
        )
        service.save()
        self.assertEqual(FreelanceService.objects.count(), 1)

    def test_service_model_optional_fields(self):
        """ Test freelance service model
        with optional fields """

        # Create user
        User = get_user_model()
        user = User.objects.create(
            first_name='Jon',
            last_name='Smith',
            email='test@mail.com',
            date_of_birth='1998-01-01',
            phone_number='+441234567890',
            password='secret',
        )

        # Test Service model
        service = FreelanceService.objects.create(
            user=user,
            category_name='WEB',
            service_headline='Test headline',
            service_search_tags='Hey,there',
            service_description='Testing the service description',
            enable_all_packages=False,
            faq_question='Can you work with Django?',
            faq_answer='Yes, I also do manual testing and document my findings.',
            basic_package_title='Here is the basic package in a few words',
            basic_delivery_time=1,
            basic_revisions=1,
            basic_details='Here are is additional information',
            basic_price=15,
            standard_package_title='',
            standard_delivery_time=None,
            standard_revisions=None,
            standard_details='',
            standard_price=None,
            premium_package_title='',
            premium_delivery_time=None,
            premium_revisions=None,
            premium_details='',
            premium_price=None,
            service_image='',
        )
        service.save()
        self.assertEqual(FreelanceService.objects.count(), 1)

    def test_service_form_is_valid(self):
        """ Test freelance service form """

        data = {
            'category_name': 'WEB',
            'service_headline': 'Test headline',
            'service_search_tags': 'testing',
            'service_description': 'Testing the service description',
            'enable_all_packages': True,
            'faq_question': '',
            'faq_answer': '',
            'basic_package_title': 'Here is the basic package in a few words',
            'basic_delivery_time': 1,
            'basic_revisions': 1,
            'basic_details': 'Here are is additional information',
            'basic_price': 15,
            'standard_package_title': '',
            'standard_delivery_time': None,
            'standard_revisions': None,
            'standard_details': '',
            'standard_price': None,
            'premium_package_title': '',
            'premium_delivery_time': None,
            'premium_revisions': None,
            'premium_details': '',
            'premium_price': None,
            'service_image': '',
        }

        form = FreelanceServiceForm(data)
        self.assertTrue(form.is_valid())

    def test_service_form_optional_fields(self):
        """ Test freelance service form
        with optional fields """

        data = {
            'category_name': 'WEB',
            'service_headline': 'Test headline',
            'service_search_tags': 'Hey,there',
            'service_description': 'Testing the service description',
            'enable_all_packages': False,
            'faq_question': 'Can you work with Django?',
            'faq_answer': 'Yes, I also do manual testing and document my findings.',
            'basic_package_title': 'Here is the basic package in a few words',
            'basic_delivery_time': 1,
            'basic_revisions': 1,
            'basic_details': 'Here are is additional information',
            'basic_price': 15,
            'basic_package_title': 'Here is the basic package in a few words',
            'basic_delivery_time': 1,
            'basic_revisions': 1,
            'basic_details': 'Here are is additional information',
            'basic_price': 15,
            'standard_package_title': '',
            'standard_delivery_time': '',
            'standard_revisions': '',
            'standard_details': '',
            'standard_price': '',
            'premium_package_title': '',
            'premium_delivery_time': '',
            'premium_revisions': '',
            'premium_details': '',
            'premium_price': '',
            'service_image': '',
        }

        form = FreelanceServiceForm(data)
        self.assertTrue(form.is_valid())

    def test_create_multiple_models_with_same_user(self):
        # Create user
        User = get_user_model()
        user = User.objects.create(
            first_name='Jon',
            last_name='Smith',
            email='test@mail.com',
            date_of_birth='1998-01-01',
            phone_number='+441234567890',
            password='secret',
        )

        # Test Service model
        service1 = FreelanceService.objects.create(
            user=user,
            category_name='WEB',
            service_headline='Test headline',
            service_search_tags='Hey,there',
            service_description='Testing the service description',
            enable_all_packages=False,
            faq_question='Can you work with Django?',
            faq_answer='Yes, I also do manual testing and document my findings.',
            basic_package_title='Here is the basic package in a few words',
            basic_delivery_time=1,
            basic_revisions=1,
            basic_details='Here are is additional information',
            basic_price=15,
            standard_package_title='',
            standard_delivery_time=None,
            standard_revisions=None,
            standard_details='',
            standard_price=None,
            premium_package_title='',
            premium_delivery_time=None,
            premium_revisions=None,
            premium_details='',
            premium_price=None,
            service_image='',
        )
        service2 = FreelanceService.objects.create(
            user=user,
            category_name='WEB',
            service_headline='Test headline',
            service_search_tags='Hey,there',
            service_description='Testing the service description',
            enable_all_packages=False,
            faq_question='Can you work with Django?',
            faq_answer='Yes, I also do manual testing and document my findings.',
            basic_package_title='Here is the basic package in a few words',
            basic_delivery_time=1,
            basic_revisions=1,
            basic_details='Here are is additional information',
            basic_price=15,
            standard_package_title='',
            standard_delivery_time=None,
            standard_revisions=None,
            standard_details='',
            standard_price=None,
            premium_package_title='',
            premium_delivery_time=None,
            premium_revisions=None,
            premium_details='',
            premium_price=None,
            service_image='',
        )
        service1.save()
        service2.save()
        self.assertEqual(FreelanceService.objects.count(), 2)
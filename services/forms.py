from django import forms
from .models import FreelanceService


class FreelanceServiceForm(forms.ModelForm):
    class Meta:
        model = FreelanceService
        exclude = ('user',)

        labels = {
            'service_category': '',
            'service_subcategory': '',
            'service_headline': '',
            'service_search_tags': '',
            'service_description': 'Description',
            'faq_question': 'Question',
            'faq_answer': 'Answer',
            'enable_all_packages': '',
            'basic_package_title': 'Package Title',
            'basic_delivery_time': 'Delivery Time',
            'basic_revisions': 'Number of Revisions',
            'basic_details': 'Additional Details',
            'basic_price': 'Price',
            'standard_package_title': 'Package Title',
            'standard_delivery_time': 'Delivery Time',
            'standard_revisions': 'Number of Revisions',
            'standard_details': 'Additional Details',
            'standard_price': 'Price',
            'premium_package_title': 'Package Title',
            'premium_delivery_time': 'Delivery Time',
            'premium_revisions': 'Number of Revisions',
            'premium_details': 'Additional Details',
            'premium_price': 'Price',
            'service_image': '',
        }

        widgets = {
            'service_search_tags': forms.HiddenInput(),
        }

    def __init__(self, *args, **kwargs):
        """ Add placeholders and classes to form inputs """

        super().__init__(*args, **kwargs)

        placeholders = {
            'service_category': 'Category',
            'service_subcategory': 'Subcategory',
            'service_headline': 'Headline',
            'service_search_tags': 'Search tags',
            'service_description': 'Describe what service you are offering',
            'faq_question': 'E.g. Can you work with Django?',
            'enable_all_packages': '',
            'faq_answer': 'Yes, I also do manual testing and document my findings.',
            'basic_package_title': 'Describe the package in a few words',
            'basic_delivery_time': 'Delivery Time',
            'basic_revisions': 'Select Revisions',
            'basic_details': 'Add any additional information here so that your clients know what to expect from this package.',
            'basic_price': '£',
            'standard_package_title': 'Describe the package in a few words',
            'standard_delivery_time': 'Delivery Time',
            'standard_revisions': 'Select Revisions',
            'standard_details': 'Add any additional information here so that your clients know what to expect from this package.',
            'standard_price': '£',
            'premium_package_title': 'Describe the package in a few words',
            'premium_delivery_time': 'Delivery Time',
            'premium_revisions': 'Select Revisions',
            'premium_details': 'Add any additional information here so that your clients know what to expect from this package.',
            'premium_price': '£',
            'service_image': '',
        }

        for field in self.fields:
            placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder

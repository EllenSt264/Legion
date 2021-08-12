from django import forms
from django.forms.widgets import HiddenInput, Textarea
from .models import BasicPackage, FreelanceService, PremiumPackage, Service, Category, StandardPackage, SubCategory


class FreelanceServiceForm(forms.ModelForm):
    class Meta:
        model = FreelanceService
        exclude = ('user',)

        labels = {
            'category_name': '',
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
            'service_search_tags': forms.HiddenInput(
                attrs={'class': "chips-hidden-input"}),
        }

    def __init__(self, *args, **kwargs):
        """ Add placeholders and classes to form inputs """

        super().__init__(*args, **kwargs)

        placeholders = {
            'category_name': 'Category',
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

        # Overwrite category choice field as radio buttons
        categories = forms.ChoiceField(
            choices=FreelanceService.CATEGORY_CHOICES,
            widget=forms.RadioSelect(
                attrs={'class': 'radio-btn'},
            ),
            label='',
        )
        self.fields['category_name'] = categories


class ServiceForm(forms.ModelForm):
    """ A class model for adding services  """

    dev_categories = forms.ModelChoiceField(
        queryset=SubCategory.objects.filter(category=1),
        empty_label=None,
        widget=forms.RadioSelect(
            attrs={'class': 'radio-btn', 'name': 'subcategory'},
        ),
        label='',
    )
    creative_categories = forms.ModelChoiceField(
        queryset=SubCategory.objects.filter(category=2),
        empty_label=None,
        widget=forms.RadioSelect(
            attrs={'class': 'radio-btn', 'name': 'subcategory'},
        ),
        label='',
    )
    writing_categories = forms.ModelChoiceField(
        queryset=SubCategory.objects.filter(category=3),
        empty_label=None,
        widget=forms.RadioSelect(
            attrs={'class': 'radio-btn', 'name': 'subcategory'},
        ),
        label='',
    )
    translation_categories = forms.ModelChoiceField(
        queryset=SubCategory.objects.filter(category=4),
        empty_label=None,
        widget=forms.RadioSelect(
            attrs={'class': 'radio-btn', 'name': 'subcategory'},
        ),
        label='',
    )

    class Meta:
        model = Service
        exclude = ('user',)

        labels = {
            'include_client_requirements': '',
            'requirements_same_for_all': '',
            'shipping_required': '',
        }

    def save(self, commit=True):
        return super(ServiceForm, self).save(commit=commit)

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)

        categories = forms.ModelChoiceField(
            queryset=Category.objects.all(),
            widget=forms.RadioSelect(
                attrs={'class': 'radio-btn'},
            ),
            label='',
        )
        self.fields['category'] = categories
        self.fields['category'].required = False
        self.fields['subcategory'].required = False

        for field in self.fields:
            if 'categories' in field:
                self.fields[field].required = False

        self.fields['search_tags'] = forms.CharField(
            widget=HiddenInput(
                attrs={'class': 'chips-hidden-input'},
            ),
        )


class BasicPackageForm(forms.ModelForm):
    class Meta:
        model = BasicPackage
        exclude = ('service',)

        labels = {
            'enable_all_packages': '',
        }


class StandardPackageForm(forms.ModelForm):
    class Meta:
        model = StandardPackage
        exclude = ('service',)


class PremiumPackageForm(forms.ModelForm):
    class Meta:
        model = PremiumPackage
        exclude = ('service',)

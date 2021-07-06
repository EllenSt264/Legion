from django import forms
from .models import UserProfile, Recruiter


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        exclude = ('user', 'recruiter',)

        labels = {
            'title': '',
            'overview': '',
            'image': 'Profile Image',
            'is_recruiter': '',
            'is_creator': '',
        }

    def __init__(self, *args, **kwargs):
        """ Add placeholders and classes to form inputs """

        super().__init__(*args, **kwargs)

        placeholders = {
            'title': 'Title',
            'overview': 'Overview',
            'image': 'Image',
            'is_recruiter': '',
            'is_creator': '',
        }

        for field in self.fields:
            placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder


class RecruiterForm(forms.ModelForm):
    class Meta:
        model = Recruiter
        exclude = ('profile',)

        labels = {
            'is_recruiter': '',
            'company_name': '',
            'town_or_city': '',
            'postcode': '',
            'country': ''
        }

    def __init__(self, *args, **kwargs):
        """ Add placeholders and classes to form inputs """

        super().__init__(*args, **kwargs)

        placeholders = {
            'is_recruiter': '',
            'company_name': 'Company Name',
            'town_or_city': 'Town or City',
            'postcode': 'Postcode',
            'country': 'Select Country',
        }

        for field in self.fields:
            if field != 'country':
                placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder

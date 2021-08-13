from django import forms
from .models import (Creator, UserProfile, Recruiter, CreatorWork,
                     Education, WorkExperience, Languages)
from services.models import Category, SubCategory


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        exclude = ('user', 'is_creator',)

        labels = {
            'title': '',
            'overview': '',
            'image': 'Profile Image',
            'is_recruiter': '',
        }

    def __init__(self, *args, **kwargs):
        """ Add placeholders and classes to form inputs """

        super().__init__(*args, **kwargs)

        placeholders = {
            'title': 'Title',
            'overview': 'Overview',
            'image': 'Image',
            'is_recruiter': '',
        }

        for field in self.fields:
            placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder


class RecruiterForm(forms.ModelForm):
    class Meta:
        model = Recruiter
        exclude = ('profile',)

        labels = {
            'company_name': '',
            'town_or_city': '',
            'postcode': '',
            'country': ''
        }

    def __init__(self, *args, **kwargs):
        """ Add placeholders and classes to form inputs """

        super().__init__(*args, **kwargs)

        placeholders = {
            'company_name': 'Company Name',
            'town_or_city': 'Town or City',
            'postcode': 'Postcode',
            'country': 'Select Country',
        }

        for field in self.fields:
            if field != 'country':
                placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder


class CreatorForm(forms.ModelForm):
    class Meta:
        model = Creator
        exclude = ('profile', 'creator_work', 'education',
                   'work_experience', 'languages')

        labels = {
            'town_or_city': '',
            'postcode': '',
            'country': ''
        }

    def __init__(self, *args, **kwargs):
        """ Add placeholders and classes to form inputs """

        super().__init__(*args, **kwargs)

        placeholders = {
            'town_or_city': 'Town or City',
            'postcode': 'Postcode',
        }

        for field in self.fields:
            if field != 'country':
                placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder


class CreatorWorkForm(forms.ModelForm):

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
        model = CreatorWork
        exclude = ('profile', 'creator',)

        widgets = {
            'skills': forms.HiddenInput(
                attrs={'class': "chips-hidden-input"}),
        }

        labels = {
            'skills': '',
        }

    def save(self, commit=True):
        return super(CreatorWorkForm, self).save(commit=commit)

    def __init__(self, *args, **kwargs):
        """ Add placeholders and classes to form inputs """

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

        # Overwrite choice field as radio buttons
        expertise = CreatorWork.Expertise
        expertise_level = forms.ChoiceField(
            choices=expertise.choices,
            widget=forms.RadioSelect(
                attrs={'class': 'radio-btn'},
            ),
            label=''
        )
        self.fields['expertise_level'] = expertise_level


class EducationForm(forms.ModelForm):
    class Meta:
        model = Education
        exclude = ('profile', 'creator')

        labels = {
            'institution_name': 'Instution Name',
            'area_of_study': 'Area of Study',
            'qualification': 'Qualification',
            'start_date': 'From',
            'end_date': 'To',
            'description': 'Description'
        }

    def __init__(self, *args, **kwargs):
        """ Add placeholders and classes to form inputs """

        super().__init__(*args, **kwargs)

        placeholders = {
            'institution_name': 'Eg. University of London',
            'area_of_study': 'Eg. Computer Science',
            'qualification': 'Eg. Bachelor',
            'start_date': 'From',
            'end_date': 'To',
            'description': 'Describe your studies, awards etc.'
        }

        for field in self.fields:
            placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder


class WorkExperienceForm(forms.ModelForm):
    class Meta:
        model = WorkExperience
        exclude = ('profile', 'creator_work')

        labels = {
            'company_name': 'Company *',
            'work_town_or_city': 'Location *',
            'work_country': '',
            'job_title': 'Job Title',
            'start_date': 'From',
            'end_date': 'To',
            'currently_working_here': '',
            'description': 'Description'
        }

    def __init__(self, *args, **kwargs):
        """ Add placeholders and classes to form inputs """

        super().__init__(*args, **kwargs)

        placeholders = {
            'company_name': 'Company Name',
            'work_town_or_city': 'Town or City',
            'job_title': '',
            'start_date': '',
            'end_date': '',
            'currently_working_here': '',
            'description': '',
        }

        for field in self.fields:
            if field != 'work_country':
                placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder


class LanguagesForm(forms.ModelForm):
    class Meta:
        model = Languages
        exclude = ('profile', 'creator')

        labels = {
            'english_proficiency': 'What is your English proficiency? *',
            'language': 'Language',
            'language_proficiency': 'Select Proficiency'
        }

    def __init__(self, *args, **kwargs):
        """ Add placeholders and classes to form inputs """

        super().__init__(*args, **kwargs)

        placeholders = {
            'english_proficiency': 'English Proficiency',
            'language': 'Select Language',
            'language_proficiency': 'Select Proficiency'
        }

        for field in self.fields:
            placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder

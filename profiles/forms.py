from django import forms
from .models import UserRecruiter


class UserRecruiterForm(forms.ModelForm):
    class Meta:
        model = UserRecruiter
        exclude = ('user',)

    def __init__(self, *args, **kwargs):
        """ Add placeholders and classes to form inputs """

        super().__init__(*args, **kwargs)

        self.fields['company_name'].widget.attrs['placeholder'] = "Company Name"
        self.fields['company_name'].label = ""
        self.fields['is_recruiter'].label = ""
        self.fields['is_client'].widget = forms.HiddenInput()

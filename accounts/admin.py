from django import forms
from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.core.exceptions import ValidationError
import datetime

from .models import User


class UserCreationForm(forms.ModelForm):
    """ A form for creating new users. Includes all the required fields,
     including  a repeated password """

    # Custom validation error for date of birth field
    def validate_date_of_birth(value):
        # Grab today's date
        todayDate = datetime.datetime.now()
        yy = todayDate.year
        mm = todayDate.month
        dd = todayDate.day

        # Users must be at least 16 to register
        maxiumDate = f'{yy-16}-{mm}-{dd}'

        if value > maxiumDate:
            raise ValidationError("You must be at least 16 to register")
        else:
            return value

    password1 = forms.CharField(
        label='Password',
        widget=forms.PasswordInput,
    )
    password2 = forms.CharField(
        label='Confirm Password',
        widget=forms.PasswordInput,
    )
    # Override date field for materialize compatibility
    date_of_birth = forms.CharField(
        label='Date of Birth',
        validators=[validate_date_of_birth],
        widget=forms.TextInput(
            attrs={
                'class': 'datepicker',
                'placeholder': 'Date of Birth',
            })
    )

    class Meta:
        model = User
        widgets = {
            # Apply placeholders
            'first_name': forms.TextInput(
                attrs={'placeholder': 'First Name'}),
            'last_name': forms.TextInput(
                attrs={'placeholder': 'Last Name'}),
            'email': forms.EmailInput(
                attrs={'placeholder': 'Email Address'}),
            'phone_number': forms.TextInput(
                attrs={'placeholder': 'Phone Number'}),
            'password1': forms.TextInput(
                attrs={'placeholder': 'Password'}),
        }
        fields = ('first_name', 'last_name', 'email',
                  'date_of_birth', 'phone_number')

    # Apply placeholders to password fields
    def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args, **kwargs)
        self.fields['password1'].widget = forms.PasswordInput(
            attrs={'placeholder': 'Password'})
        self.fields['password2'].widget = forms.PasswordInput(
            attrs={'placeholder': 'Confirm Password'})

    def clean_password2(self):
        # Check that passwords match
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise ValidationError("Passwords don't match!")
        return password2

    def save(self, commit=True):
        # Save password in hashed format
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    """ A form for updating users. Includes all fields but replaces
     the password field with admin's disabled password hash display field. """
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'password',
                  'date_of_birth', 'phone_number',
                  'is_active', 'is_admin')


class UserAdmin(BaseUserAdmin):
    # The forms to add and change user instances
    form = UserChangeForm
    add_form = UserCreationForm

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ('email', 'first_name', 'last_name', 'is_admin')
    list_filter = ('is_admin',)
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name',
                                      'date_of_birth', 'phone_number',)}),
        ('Permissions', {'fields': ('is_admin',)}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('first_name', 'last_name', 'email', 'date_of_birth',
                       'phone_number', 'password1', 'password2'),
        }),
    )
    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ()


# Register the new UserAdmin
admin.site.register(User, UserAdmin)
# Unregister the group model from admin
admin.site.unregister(Group)

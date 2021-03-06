from django import forms
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .models import (Creator, UserProfile, Recruiter, CreatorWork,
                     Education, WorkExperience, Languages)

from .forms import UserProfileForm


class UserProfileChangeForm(forms.ModelForm):
    """ A form for updating users. Includes all fields but replaces
     the password field with admin's disabled password hash display field. """

    class Meta:
        model = UserProfile
        fields = ('user', 'title', 'overview', 'image',
                  'is_recruiter', 'is_creator')


class RecruiterInlineForm(admin.StackedInline):
    model = Recruiter
    extra = 0


class CreatorInlineForm(admin.StackedInline):
    model = Creator
    extra = 0


class CreatorWorkInlineForm(admin.StackedInline):
    model = CreatorWork
    extra = 0


class EducationInlineForm(admin.StackedInline):
    model = Education
    extra = 0


class WorkExperienceInlineForm(admin.StackedInline):
    model = WorkExperience
    extra = 0


class LanguagesInlineForm(admin.StackedInline):
    model = Languages
    extra = 0


class UserProfileAdmin(admin.ModelAdmin):
    # The forms to add and change user instances
    form = UserProfileChangeForm
    add_form = UserProfileForm

    inline_type = 'tabular'
    inlines = [
        RecruiterInlineForm,
        CreatorInlineForm,
        CreatorWorkInlineForm,
        EducationInlineForm,
        WorkExperienceInlineForm,
        LanguagesInlineForm
    ]

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ('user', 'is_recruiter', 'is_creator',)
    fieldsets = (
        ('Personal info', {'fields': ('user', 'title',
                                      'overview', 'image',)}),
        ('Permissions', {'fields': ('is_recruiter', 'is_creator')}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('user', 'title', 'overview', 'image',),
        }),
    )
    search_fields = ('user',)
    ordering = ('user',)
    filter_horizontal = ()


admin.site.register(UserProfile, UserProfileAdmin)

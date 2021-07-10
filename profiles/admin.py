from django import forms
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .models import (Creator, UserProfile, Recruiter,
                     CreatorWork, Category,
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


class CreatorInlineForm(admin.StackedInline):
    model = Creator


class CreatorWorkInlineForm(admin.StackedInline):
    model = CreatorWork

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "category":
            parent_id = request.resolver_match.kwargs['object_id']
            kwargs["queryset"] = Category.objects.filter(category_name=parent_id)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


class CategoryInlineForm(admin.StackedInline):
    model = Category


class EducationInlineForm(admin.StackedInline):
    model = Education


class WorkExperienceInlineForm(admin.StackedInline):
    model = WorkExperience


class LanguagesInlineForm(admin.StackedInline):
    model = Languages


class UserProfileAdmin(admin.ModelAdmin):
    # The forms to add and change user instances
    form = UserProfileChangeForm
    add_form = UserProfileForm

    inline_type = 'tabular'
    inlines = [
        RecruiterInlineForm,
        CreatorInlineForm,
        CategoryInlineForm,
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

from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required

from .models import UserProfile
from .forms import (RecruiterForm, UserProfileForm, CreatorForm,
                    CreatorWorkForm, CategoryForm,
                    EducationForm, WorkExperienceForm, LanguagesForm)


@login_required
def start(request):
    """ A view to render the get started page """
    return render(request, 'profiles/get-started.html')


@login_required
def start_creator(request):
    """ A view to render the get started page """

    return render(request, 'profiles/creator-get-started.html')


@login_required
def creator_form(request, user_id):
    """ A view to render the creator form """

    user = get_object_or_404(get_user_model(), pk=user_id)
    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        profile_form = UserProfileForm(request.POST, instance=profile)
        creator_form = CreatorForm(request.POST)
        work_form = CreatorWorkForm(request.POST)
        category_form = CategoryForm(request.POST)
        education_form = EducationForm(request.POST)
        work_experience_form = WorkExperienceForm(request.POST)
        languages_form = LanguagesForm(request.POST)

        form_list = [
            profile_form, creator_form, work_form,
            category_form,
            education_form, work_experience_form,
            languages_form
        ]

        for each_form in form_list:
            if each_form.is_valid():
                profile = profile_form.save(commit=False)
                creator = creator_form.save(commit=False)
                creator.profile = profile
                profile.save()
                creator.save()

                category = category_form.save(commit=False)
                category.save()

                creator_work = work_form.save(commit=False)
                creator_work.profile = profile
                creator_work.category = category
                creator_work.save()

                education = education_form.save(commit=False)
                education.profile = profile
                education.save()

                work = work_experience_form.save(commit=False)
                work.profile = profile
                work.save()

                languages = languages_form.save(commit=False)
                languages.profile = profile
                languages.save()

                return redirect(reverse('success_client'))
            else:
                return redirect(reverse('fail'))
    else:
        profile_form = UserProfileForm(instance=profile)
        creator_form = CreatorForm()
        work_form = CreatorWorkForm()
        category_form = CategoryForm()
        education_form = EducationForm()
        work_experience_form = WorkExperienceForm()
        languages_form = LanguagesForm()

    template = 'profiles/creator-form.html'
    context = {
        'user': user,
        'profile_form': profile_form,
        'creator_form': creator_form,
        'category_form': category_form,
        'work_form': work_form,
        'education_form': education_form,
        'work_experience_form': work_experience_form,
        'languages_form': languages_form,
    }

    return render(request, template, context)


@login_required
def start_client(request):
    """ A view to render the get started page and
    update the user's profile with recruiter data if applicable """

    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        profile_form = UserProfileForm(request.POST, instance=profile)
        recruiter_form = RecruiterForm(request.POST)

        if profile_form.is_valid() and recruiter_form.is_valid():
            form = profile_form.save(commit=False)
            recruiter = recruiter_form.save(commit=False)
            recruiter.profile = form
            form.save()
            recruiter.save()
            return redirect(reverse('success_client'))
        else:
            return redirect(reverse('fail'))
    else:
        profile_form = UserProfileForm(instance=profile)
        recruiter_form = RecruiterForm()

    template = 'profiles/client-get-started.html'
    context = {
        'profile_form': profile_form,
        'form': recruiter_form,
    }

    return render(request, template, context)


@login_required
def success_creator(request):
    """ A view to render the success page
     for when a creator completes their profile """

    return render(request, 'profiles/success-creator.html')


@login_required
def success_client(request):
    """ A view to render the success page
     for when a client completes their profile """

    return render(request, 'profiles/success-client.html')


@login_required
def fail(request):
    return render(request, 'profiles/fail.html')

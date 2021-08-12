from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth import get_user_model
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import (UserProfile, Recruiter, Creator,
                     CreatorWork, Education, WorkExperience,
                     Languages)
from .forms import (RecruiterForm, UserProfileForm,
                    CreatorForm, CreatorWorkForm,
                    EducationForm, WorkExperienceForm,
                    LanguagesForm)


# ==========================================================
# Profile setup - Get Started pages
# ==========================================================

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
        education_form = EducationForm(request.POST)
        work_experience_form = WorkExperienceForm(request.POST)
        languages_form = LanguagesForm(request.POST)

        form_list = [
            profile_form, creator_form, work_form,
            education_form, work_experience_form,
            languages_form
        ]

        for each_form in form_list:
            if each_form.is_valid() is False:
                return redirect(reverse('fail'))

        if profile_form.is_valid():
            profile = profile_form.save(commit=False)
            profile.is_creator = True

        if creator_form.is_valid():
            creator = creator_form.save(commit=False)
            creator.profile = profile
            profile.save()
            creator.save()

        if work_form.is_valid():
            field = None
            try:
                if work_form.cleaned_data['dev_categories']:
                    field = work_form.cleaned_data['dev_categories']
                elif work_form.cleaned_data['creative_categories']:
                    field = work_form.cleaned_data['creative_categories']
                elif work_form.cleaned_data['writing_categories']:
                    field = work_form.cleaned_data['writing_categories']
                elif work_form.cleaned_data['translation_categories']:
                    field = work_form.cleaned_data['translation_categories']
            except Exception as e:
                messages.error(request, 'Error! {e} The form could not be validated. \
                        Please try again.').format(e)

            creator_work = work_form.save(commit=False)
            creator_work.profile = profile
            creator_work.subcategory = field
            creator_work.save()

        if education_form.is_valid():
            education = education_form.save(commit=False)
            education.profile = profile
            education.save()

        if work_experience_form.is_valid():
            work = work_experience_form.save(commit=False)
            work.profile = profile
            work.save()

        if languages_form.is_valid():
            languages = languages_form.save(commit=False)
            languages.profile = profile
            languages.save()

        return redirect(reverse('success_creator'))  
    else:
        profile_form = UserProfileForm(instance=profile)
        creator_form = CreatorForm()
        work_form = CreatorWorkForm()
        education_form = EducationForm()
        work_experience_form = WorkExperienceForm()
        languages_form = LanguagesForm()

    template = 'profiles/creator-form.html'
    context = {
        'user': user,
        'profile_form': profile_form,
        'creator_form': creator_form,
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
        profile_form = UserProfileForm(
            request.POST, request.FILES, instance=profile)
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


# ==========================================================
# User Profile pages
# ==========================================================

@login_required
def profile_or_redirect(request):
    """ A view to direct users to their profile or redirect them to
    the Get Started pages if their profile has not been completed """

    profile = get_object_or_404(UserProfile, user=request.user)
    if profile.is_creator or profile.is_recruiter:
        return redirect(reverse(user_profile, args=(request.user.pk,)))
    else:
        return redirect(reverse('start'))


@login_required
def user_profile(request, user_id):
    """ A view to render the profile page """

    if request.user.is_authenticated:
        user = get_object_or_404(get_user_model(), pk=user_id)
        if request.user.pk == user.pk:
            profile = get_object_or_404(UserProfile, user=request.user)

            if profile.is_recruiter:
                recruiter = get_object_or_404(Recruiter, profile=profile)

                template = 'profiles/userprofile.html'
                context = {
                    'profile': profile,
                    'recruiter': recruiter
                }
                return render(request, template, context)
            else:
                creator = get_object_or_404(Creator, profile=profile)
                work = get_object_or_404(CreatorWork, profile=profile)
                education = get_object_or_404(Education, profile=profile)
                workexperience = get_object_or_404(
                    WorkExperience, profile=profile)
                languages = get_object_or_404(Languages, profile=profile)

                template = 'profiles/userprofile.html'
                context = {
                    'profile': profile,
                    'creator': creator,
                    'work': work,
                    'education': education,
                    'workexperience': workexperience,
                    'languages': languages,
                }
                return render(request, template, context)
        else:
            print('You are not authorised to be here!')
            return redirect(reverse('home'))

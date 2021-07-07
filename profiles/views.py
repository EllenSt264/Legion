from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required

from .models import UserProfile
from .forms import RecruiterForm, UserProfileForm


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

    template = 'profiles/creator-form.html'
    context = {
        'user': user,
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
        recruiter_form = RecruiterForm(instance=profile)

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

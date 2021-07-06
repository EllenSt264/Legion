from django.shortcuts import render, redirect, reverse, get_object_or_404
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
def start_client(request):
    """ A view to render the get started page and
    update the user's profile with recruiter data if applicable """

    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        form2 = RecruiterForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            form2.save()
            return redirect(reverse('success_client'))
        else:
            return redirect(reverse('fail'))
    else:
        form = UserProfileForm(instance=profile)
        form2 = RecruiterForm(instance=profile)

    template = 'profiles/client-get-started.html'
    context = {
        'profile_form': form,
        'form': form2,
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

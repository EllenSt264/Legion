from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import UserProfile
from .forms import UserRecruiterForm


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

    form = UserRecruiterForm()

    template = 'profiles/client-get-started.html'
    context = {
        'form': form
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

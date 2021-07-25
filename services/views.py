from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required

from .forms import FreelanceServiceForm
from .models import FreelanceService
from profiles.models import UserProfile


def services(request):
    """ A view to display all services, including
    sorting and searching queries """

    services = FreelanceService.objects.all()
    creator_profile = UserProfile.objects.all()

    template = 'services/services.html'
    context = {
        'services': services,
        'creator_profile': creator_profile,
    }

    return render(request, template, context)


@login_required
def add_service(request, user_id):
    """ A view to render the form for creators to add new services """

    user = get_object_or_404(get_user_model(), pk=user_id)

    if request.method == 'POST':
        form = FreelanceServiceForm(request.POST, request.FILES)
        if form.is_valid():
            service = form.save(commit=False)
            service.user = request.user
            service.save()
            messages.success(request, 'Successfully added service!')
            return redirect(reverse('profile_or_redirect'))
        else:
            for field, error in form.errors.items():
                messages.error(
                    request, 'Error! Form field: "{}" {}'.format(
                        field, ','.join(error).replace('This field', ''))
                )
    else:
        form = FreelanceServiceForm()

    template = 'services/freelance-form.html'
    context = {
        'form': form,
    }

    return render(request, template, context)

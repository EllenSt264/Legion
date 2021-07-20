from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required

from .forms import FreelanceServiceForm


@login_required
def add_service(request, user_id):
    """ A view to render the form for creators to add new services """

    user = get_object_or_404(get_user_model(), pk=user_id)

    if request.method == 'POST':
        form = FreelanceServiceForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            service = form.save()
            messages.success(request, 'Successfully added service!')
            return redirect(reverse('profile_or_redirect'))
        else:
            messages.error(request, 'There was an error with your form. \
                Please double check your information.')
            return redirect(reverse('home'))
    else:
        form = FreelanceServiceForm()

    template = 'services/freelance-form.html'
    context = {
        'form': form,
    }

    return render(request, template, context)

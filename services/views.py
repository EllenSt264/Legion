from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required

from .forms import BasicPackageForm, PremiumPackageForm, ServiceForm, StandardPackageForm
from .models import FreelanceService, Service
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


def service_details(request, service_id):
    """ A view to display individual service details """

    service = get_object_or_404(FreelanceService, pk=service_id)

    template = 'services/service-details.html'
    context = {
        'service': service,
    }

    return render(request, template, context)


@login_required
def add_service(request, user_id):
    """ A view to render the form for creators to add new services """

    if request.method == "POST":
        form = ServiceForm(request.POST, request.FILES)
        if form.is_valid():
            # Determine what subcategory form field was used and update
            # the service subcategory field with that value
            field = None
            try:
                if form.cleaned_data['dev_categories']:
                    field = form.cleaned_data['dev_categories']
                elif form.cleaned_data['creative_categories']:
                    field = form.cleaned_data['creative_categories']
                elif form.cleaned_data['writing_categories']:
                    field = form.cleaned_data['writing_categories']
                elif form.cleaned_data['translation_categories']:
                    field = form.cleaned_data['translation_categories']
            except Exception as e:
                messages.error(request, 'Error! {e} The form could not be validated. \
                     Please try again.').format(e)

            service = form.save(commit=False)
            service.subcategory = field
            service.user = request.user
            service.save()

            user_service = Service.objects.get(
                user=request.user, pk=service.pk)
            service_id = user_service.pk

            return redirect(reverse(
                'add_service_part_two',
                args=(request.user.pk, service_id,)
                ))
        else:
            for field, error in form.errors.items():
                messages.error(
                    request, 'Error! Form field: "{}" {}'.format(
                        field, ','.join(error).replace('This field', ''))
                )
    else:
        form = ServiceForm()

    template = 'services/add-service-form.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def add_service_part_two(request, user_id, service_id):
    """ A view to render the form for creators to add new services """

    service = get_object_or_404(Service, user=request.user, pk=service_id)

    if request.method == 'POST':
        basic_package_form = BasicPackageForm(request.POST)
        standard_package_form = StandardPackageForm(request.POST)
        premium_package_form = PremiumPackageForm(request.POST)

        form_list = [
            basic_package_form, standard_package_form,
            premium_package_form
        ]

        for form in form_list:
            if form.is_valid():
                package = form.save(commit=False)
                package.service = service
                package.save()

                messages.success(request, 'Successfully added service!')
                return redirect(reverse('profile_or_redirect'))
            else:
                for field, error in form.errors.items():
                    messages.error(
                        request, 'Error! Form field: "{}" {}'.format(
                            field, ','.join(error).replace('This field', ''))
                    )
    else:
        basic_package_form = BasicPackageForm()
        standard_package_form = StandardPackageForm()
        premium_package_form = PremiumPackageForm()

    template = 'services/add-service-form-packages.html'
    context = {
        'service': service,
        'basic_package_form': basic_package_form,
        'standard_package_form': standard_package_form,
        'premium_package_form': premium_package_form,
    }

    return render(request, template, context)

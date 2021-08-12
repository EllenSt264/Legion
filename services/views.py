from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required

from .forms import (ServiceForm, BasicPackageForm,
                    PremiumPackageForm, StandardPackageForm)
from .models import Category, Service
from profiles.models import UserProfile


def services(request):
    """ A view to display all services, including
    sorting and searching queries """

    services = Service.objects.all()
    creator_profile = UserProfile.objects.all()

    template = 'services/services.html'
    context = {
        'services': services,
        'creator_profile': creator_profile,
    }

    return render(request, template, context)


def service_details(request, service_id):
    """ A view to display individual service details """

    service = get_object_or_404(Service, pk=service_id)
    creator_profile = UserProfile.objects.all()

    template = 'services/service-details.html'
    context = {
        'service': service,
        'creator_profile': creator_profile,
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
                    categoryVal = 1
                elif form.cleaned_data['creative_categories']:
                    field = form.cleaned_data['creative_categories']
                    categoryVal = 2
                elif form.cleaned_data['writing_categories']:
                    field = form.cleaned_data['writing_categories']
                    categoryVal = 3
                elif form.cleaned_data['translation_categories']:
                    field = form.cleaned_data['translation_categories']
                    categoryVal = 4
            except Exception as e:
                messages.error(request, 'Error! {e} The form could not be validated. \
                     Please try again.').format(e)

            service = form.save(commit=False)
            service.category = Category.objects.get(pk=categoryVal)
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
        basic_data = {
            'package_title': request.POST.get('package_title'),
            'package_description': request.POST.get('package_description'),
            'client_requirements': request.POST.get('client_requirements'),
            'delivery_time': request.POST.get('delivery_time'),
            'revisions': request.POST.get('revisions'),
            'price': request.POST.get('price'),
            'fast_delivery_time': request.POST.get('fast_delivery_time'),
            'fast_delivery_price': request.POST.get('fast_delivery_price'),
            'reference_images': request.POST.get('reference_images'),
        }
        basic_package_form = BasicPackageForm(basic_data)

        standard_data = {
            'package_title': request.POST.get('standard_package_title'),
            'package_description': request.POST.get('standard_package_description'),
            'client_requirements': request.POST.get('standard_client_requirements'),
            'delivery_time': request.POST.get('standard_delivery_time'),
            'revisions': request.POST.get('standard_revisions'),
            'price': request.POST.get('standard_price'),
            'fast_delivery_time': request.POST.get('standard_fast_delivery_time'),
            'fast_delivery_price': request.POST.get('standard_fast_delivery_price'),
            'reference_images': request.POST.get('standard_reference_images'),
        }
        standard_package_form = StandardPackageForm(standard_data)

        premium_data = {
            'package_title': request.POST.get('premium_package_title'),
            'package_description': request.POST.get('premium_package_description'),
            'client_requirements': request.POST.get('premium_client_requirements'),
            'delivery_time': request.POST.get('premium_delivery_time'),
            'revisions': request.POST.get('premium_revisions'),
            'price': request.POST.get('premium_price'),
            'fast_delivery_time': request.POST.get('premium_fast_delivery_time'),
            'fast_delivery_price': request.POST.get('premium_fast_delivery_price'),
            'reference_images': request.POST.get('premium_reference_images'),
        }
        premium_package_form = PremiumPackageForm(premium_data)

        basic = basic_package_form
        standard = standard_package_form
        premium = premium_package_form

        if basic.is_valid() and standard.is_valid and premium.is_valid():

            basic_package = basic.save(commit=False)
            basic_package.service = service
            standard_package = standard.save(commit=False)
            standard_package.service = service
            premium_package = premium.save(commit=False)
            premium_package.service = service

            basic_package.save()
            standard_package.save()
            premium_package.save()

            messages.success(request, 'Successfully added service!')
            return redirect(reverse('profile_or_redirect'))
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

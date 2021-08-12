from django.shortcuts import get_object_or_404

from .models import Creator, Recruiter, UserProfile


def profile_processor(request):
    if request.user.is_authenticated:
        profile = get_object_or_404(UserProfile, user=request.user)
        if profile.is_creator:
            profile_contact = get_object_or_404(Creator, profile=profile)
        elif profile.is_recruiter:
            profile_contact = get_object_or_404(Recruiter, profile=profile)
        else:
            profile_contact = None
    else:
        profile = None
        profile_contact = None

    context = {
        'profile': profile,
        'profile_contact': profile_contact,
    }
    return context

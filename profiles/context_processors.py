from django.shortcuts import get_object_or_404

from .models import UserProfile


def profile_processor(request):
    profile = get_object_or_404(UserProfile, user=request.user)
    return {'profile': profile}

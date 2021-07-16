from django.shortcuts import get_object_or_404

from .models import UserProfile


def profile_processor(request):
    if request.user.is_authenticated:
        profile = get_object_or_404(UserProfile, user=request.user)
    else:
        profile = None
    return {'profile': profile}

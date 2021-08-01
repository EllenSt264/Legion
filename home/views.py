from django.shortcuts import redirect, render, get_object_or_404

from profiles.models import UserProfile


def home(request):
    """ A view to render the home page """

    if request.user.is_authenticated:
        profile = get_object_or_404(UserProfile, user=request.user)
        context = {
            'profile': profile,
        }
        template = 'home/index-authenticated.html'
        return render(request, template, context)
    else:
        return render(request, 'home/index.html')

from django.shortcuts import render


def start(request):
    """ A view to render the get started page """
    return render(request, 'profiles/get-started.html')


def start_creator(request):
    """ A view to render the get started page """
    return render(request, 'profiles/creator-get-started.html')


def start_client(request):
    """ A view to render the get started page """
    return render(request, 'profiles/client-get-started.html')

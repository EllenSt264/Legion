from django.urls import path
from django.urls.resolvers import URLPattern
from . import views

urlpatterns = [
    path('get-started/', views.start, name='start'),
    path('get-started/creator', views.start_creator, name='start_creator'),
    path('get-started/client', views.start_client, name='start_client')
]

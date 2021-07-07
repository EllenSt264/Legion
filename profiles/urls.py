from django.urls import path
from django.urls import path
from django.urls.resolvers import URLPattern
from . import views

urlpatterns = [
    path('get-started/', views.start, name='start'),
    path('get-started/creator', views.start_creator, name='start_creator'),
    path('get-started/creator/<int:user_id>', views.creator_form, name='creator_form'),
    path('get-started/client', views.start_client, name='start_client'),
    path('get-started/client/success', views.success_client, name='success_client'),
    path('get-started/creator/success', views.success_creator, name='success_creator'),
    path('get-started/fail', views.fail, name='fail')
]

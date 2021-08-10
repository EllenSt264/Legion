from django.urls import path
from django.urls.resolvers import URLPattern
from . import views
from services import views as services


urlpatterns = [
    path('', views.profile_or_redirect, name='profile_or_redirect'),
    path('get-started/', views.start, name='start'),
    path('get-started/creator', views.start_creator, name='start_creator'),
    path('get-started/creator/<int:user_id>', views.creator_form, name='creator_form'),
    path('get-started/client', views.start_client, name='start_client'),
    path('get-started/client/success', views.success_client, name='success_client'),
    path('get-started/creator/success', views.success_creator, name='success_creator'),
    path('get-started/fail', views.fail, name='fail'),
    path('<int:user_id>/', views.user_profile, name='user_profile'),
    path('<int:user_id>/add-service', services.add_service, name='add_service'),
    path('<int:user_id>/add-service/<int:service_id>/packages', services.add_service_part_two, name='add_service_part_two'),
]

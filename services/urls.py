from django.urls import path
from django.urls.resolvers import URLPattern
from . import views


urlpatterns = [
    path('', views.services, name='services'),
    path('<int:service_id>/', views.service_details, name='service_details')
]

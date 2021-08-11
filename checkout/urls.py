from django.urls import path
from django.urls.resolvers import URLPattern
from . import views


urlpatterns = [
    path('<int:service_id>/', views.checkout, name='checkout'),
]

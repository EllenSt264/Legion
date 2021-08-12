from django.urls import path
from django.urls.resolvers import URLPattern
from . import views


urlpatterns = [
    path('<int:service_id>/', views.checkout, name='checkout'),
    path('<int:service_id>/payment', views.checkout_payment, name='checkout_payment'),
    path('success/<order_number>', views.checkout_success, name='checkout_success'),
]

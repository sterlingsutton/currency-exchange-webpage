from django.urls import path
from . import views

urlpatterns = [
    path('', views.exchange_rate_list, name='exchange_rate_list'),
    path('exchange_calculator', views.exchange_calculator, name='exchange_calculator')
]
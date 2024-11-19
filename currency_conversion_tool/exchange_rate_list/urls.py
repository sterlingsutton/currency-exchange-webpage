from django.urls import path
from . import views

urlpatterns = [
    path('exchange_rate_list/', views.exchange_rate_list, name='exchange_rate_list'),
]
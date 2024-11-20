from django.shortcuts import render
from django.http import HttpResponse
import requests

# Create your views here.
def exchange_rate_list(request):
    rates = requests.get('https://api.frankfurter.app/latest')
    return HttpResponse(rates)
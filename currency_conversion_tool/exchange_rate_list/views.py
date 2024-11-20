from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
import requests

# Create your views here.
def exchange_rate_list(request):
    template = loader.get_template('exchange_rate_list.html')
    rates = requests.get('https://api.frankfurter.app/latest').json()['rates']
    context = {
        'rates': rates
    }
    return HttpResponse(template.render(context, request))
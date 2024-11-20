from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
import requests

# Create your views here.
def exchange_rate_list(request):
    template = loader.get_template('exchange_rate_list.html')
    data = requests.get('https://api.frankfurter.app/latest?base=USD').json()
    rates = data['rates']
    base = data['base']
    context = {
        'rates': rates,
        'base': base
    }
    return HttpResponse(template.render(context, request))
from django.shortcuts import render
from django.http import HttpResponse, HttpRequest

# Create your views here.
def exchange_rate_list():
    #req = HttpRequest('https://api.frankfurter.app/latest')
    #HttpResponse(req['rates'])
    HttpResponse("Hello, world!")
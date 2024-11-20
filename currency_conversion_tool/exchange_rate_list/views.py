from django.shortcuts import render
from django.http import HttpResponse, HttpRequest

# Create your views here.
def exchange_rate_list(request):
    return HttpResponse("Hello, world!")
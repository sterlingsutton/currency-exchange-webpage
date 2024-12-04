from django.shortcuts import render
import requests
from django.http import HttpResponseRedirect, HttpResponse
from .forms import CalculatorForm

# Create your views here.
def calculator(request):
    if request.method == 'POST':
        form = CalculatorForm(request.POST)
        if form.is_valid():
            data = request.POST.dict()
            base_amount = float(data.get('base_amount'))
            base_currency = data.get('base_currency')
            target_currency = data.get('target_currency')

            # perform calculation
            if base_currency != target_currency:
                exchange_rate = requests.get(f"https://api.frankfurter.dev/v1/latest?base={base_currency}").json()["rates"][target_currency]
            else:
                # if currencies are the same, then the ratio is 1:1
                exchange_rate = 1.0
            target_amount = base_amount * exchange_rate
            target_amount = round(target_amount, 2)

            return render(request, 'calculator.html', {'form': form, 'target_amount': target_amount, 'target_currency': target_currency})

    form = CalculatorForm()
    return render(request, 'calculator.html', {'form': form, 'target_amount': None, 'target_currency': None})
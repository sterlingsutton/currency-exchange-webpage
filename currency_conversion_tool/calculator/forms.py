from django import forms
import requests
import json

import requests.structures

class CalculatorForm(forms.Form):
    res = requests.get('https://api.frankfurter.app/currencies')

    currency_dict = dict((key, f"{value} ({key})") for key, value in res.json().items())
    
    base_amount = forms.FloatField(min_value=0)
    base_currency = forms.ChoiceField(choices=currency_dict, initial='USD')
    target_currency = forms.ChoiceField(choices=currency_dict, initial='EUR')
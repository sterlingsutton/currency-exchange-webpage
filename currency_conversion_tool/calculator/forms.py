from django import forms
import requests

class CalculatorForm(forms.Form):
    currency_list = requests.get('https://api.frankfurter.app/currencies').dict_keys
    base_amount = forms.FloatField(min_value=0)
    base_currency = forms.CharField(widget=forms.Select(choices=currency_list))
    target_currency = forms.CharField(widget=forms.Select(choices=currency_list))
from django import forms
import requests

class CalculatorForm(forms.Form):
    def __init__(self):
        self.currencies = requests.get('https://api.frankfurter.app/currencies')
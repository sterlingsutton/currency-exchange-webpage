import requests

def convert(amount, base, new):
    conversion = requests.get(f'https://api.frankfurter.app/latest?base={base}&symbols={new}').json()
    print(conversion['rates'][new])

convert(1, 'USD', 'EUR')

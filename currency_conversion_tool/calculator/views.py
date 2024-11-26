from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import CalculatorForm

# Create your views here.
def calculator(request):
    if request.method == 'POST':
        form = CalculatorForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect("/calculator/")
    
    else:
        form = CalculatorForm()
        
    return render(request, 'calculator.html', {'form': form})
    
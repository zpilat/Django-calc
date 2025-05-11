from django.shortcuts import render
from .forms import FactorialForm

# Create your views here.
def factorial(request):
    form = FactorialForm()
    return render(request, 'factorial.html', {'form': form})

def factorial_recursion(number):
    return 1 if number in (0, 1) else number*factorial_recursion(number-1)

def calc_factorial(request):
    form = FactorialForm(request.POST)
    if form.is_valid():
        number = form.cleaned_data['number']
        result = factorial_recursion(number)
        result = f'{result:.4e}'
        context = {'number': number, 'result': result}
        return render(request, 'partials/factorial_result.html', context)
    else:
        context = {'form': form}
        return render(request, 'partials/factorial_not_valid.html', context)

from django.shortcuts import render
from .forms import FactorialForm

# Create your views here.
def index(request):
    return render(request, 'index.html')

def factorial_modal(request):
    form = FactorialForm()
    return render(request, 'partials/factorial_modal.html', {'form': form})

def factorial_recursion(number):
    return 1 if number in (0, 1) else number*factorial_recursion(number-1)

def calc_factorial(request):
    form = FactorialForm(request.POST)
    if form.is_valid():
        number = form.cleaned_data['number']
        result = factorial_recursion(number)
        if result > 1000000000:
            result = f'{result:.4e}'
        context = {'number': number, 'result': result}
        return render(request, 'partials/factorial_result.html', context)
    else:
        context = {'form': form}
        return render(request, 'partials/factorial_not_valid.html', context)

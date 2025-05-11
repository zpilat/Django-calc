from django.shortcuts import render
from .forms import Factorial2Form

# Create your views here.
def factorial_recursion(number):
    return 1 if number in (0, 1) else number*factorial_recursion(number-1)

def factorial2(request):
    if request.method == "POST":
        form = Factorial2Form(request.POST)
        if form.is_valid():
            number = form.cleaned_data["number"]
            result = factorial_recursion(number)
            if result > 1000000000:
                result = f'{result:.4e}'
            return render(request, "factorial2.html", {
                "form": form,
                "result": result,
                "number": number,
            })
    else:
        form = Factorial2Form()  # čistý formulář při prvním načtení

    return render(request, "factorial2.html", {"form": form})

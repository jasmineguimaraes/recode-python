from django.shortcuts import render, redirect
from django.contrib import messages

from .forms import CalculoFrom

def index(request):
    return render(request, 'home.html')

def calcular(request):
    if request.method == 'POST':
        req = request.POST.copy()
        req["num1"] = request.POST["num1"].replace(",",".")
        req["num2"] = request.POST["num2"].replace(",",".")
        form = CalculoFrom(req or None)
        if (form.is_valid()):
            num1 = form.cleaned_data['num1']
            num2 = form.cleaned_data['num2']
            op = form.cleaned_data['operacao']
            if op == 1:
                resultado = num1 + num2
            elif op == 2:
                resultado = num1 - num2
            elif op == 3:
                resultado = num1 * num2
            elif op == 4:
                resultado = num1 / num2
            messages.success(request, ("Calculado com Sucesso!"))
            return render(request, 'home.html', {"resultado": resultado})
        else:
            messages.error(request, 'Houve um erro com o calculo')
            return redirect('home.html')


from django.shortcuts import render, redirect
from .models import RegisterEmployee
# Create your views here.


def home(requets):
    if requets.method == 'POST':
        names       = requets.POST['name']
        first_names = requets.POST['first-name']
        position    = requets.POST['postion']
        salarys     = requets.POST['salary']
        symbol      = requets.POST['symbol']
        
        
        new_employ = RegisterEmployee.objects.create(name=names, first_name=first_names, position_occupied=position, salary=salarys, symbols_money=symbol)
        new_employ.save()
        return redirect('home')
    return render(requets, 'index.html')
from django.shortcuts import render, redirect
from datetime import date


def index(request):    
    return render(request, 'index.html')


def today(request):    
    today = date.today()
    context = {'today': today}
    return render(request, 'today.html', context)

def table(request):  
    if 'number' in request.GET and request.GET['number'].isdigit():
        print(request.GET['number']) 
        return redirect(f"/multiply-table/{request.GET['number']}")
    else:
        return render(request, 'table.html')
    

def tables(request, number):  
    numbers = [f"{i + 1} * {number} = {(i + 1) * number}" for i in range(10)]      
    context = {'number': number, 'numbers': numbers}
    return render(request, 'tables.html', context)
from django.shortcuts import render
from datetime import date


def index(request):    
    today = date.today()
    context = {'today': today}
    return render(request, 'index.html', context)


def today(request):    
    today = date.today()
    context = {'today': today}
    return render(request, 'today.html', context)

def table(request):    
    today = date.today()
    context = {'today': today}
    return render(request, 'table.html', context)

def tables(request):    
    today = date.today()
    context = {'today': today}
    return render(request, 'tables.html', context)
from django.shortcuts import render

# Create your views here.


def add(request):
    return render(request, 'restaurants/add.html')


def all(request):
    return render(request, 'restaurants/all.html')


def change(request):
    return render(request, 'restaurants/change.html')


def find(request):
    return render(request, 'restaurants/find.html')


def index(request):
    return render(request, 'restaurants/index.html')


def view_find(request):
    return render(request, 'restaurants/view_find.html')

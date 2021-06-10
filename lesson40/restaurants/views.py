from django.shortcuts import render
from .models import Restaurants

# Create your views here.


def add(request):
    return render(request,
                  'restaurants/add.html',
                  {'title': 'Add'})


def all(request):
    restaurants = Restaurants.objects.all()
    return render(request,
                  'restaurants/all.html',
                  {
                      'title': 'All',
                      'restaurants': restaurants
                  })


def change(request):
    print(request.method)
    print(request.body)
    return render(request,
                  'restaurants/change.html',
                  {'title': 'Change'})


def find(request):
    return render(request,
                  'restaurants/find.html',
                  {'title': 'Find'})


def index(request):
    return render(request,
                  'restaurants/index.html',
                  {'title': 'Restaurants'})


def view_find(request):
    return render(request,
                  'restaurants/view_find.html',
                  {'title': 'View find'})

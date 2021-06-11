from django.shortcuts import render
from .models import Restaurants
# Create your views here.


def all(request):
    restaurants = Restaurants.work_out(request)
    return render(request,
                  'restaurants/all.html',
                  {
                      'title': 'The restorants',
                      'restaurants': restaurants
                  })

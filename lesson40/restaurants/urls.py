from django.urls import path
from .views import *

urlpatterns = [
    path('add/', add, name='home'),
    path('all/', all, name='home'),
    path('change/', change, name='home'),
    path('find/', find, name='home'),
    path('', index, name='home'),
    path('view-find/', view_find, name='home'),
]

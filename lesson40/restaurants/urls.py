from django.urls import path
from .views import *

urlpatterns = [
    path('add/', add, name='add'),
    path('all/', all, name='all'),
    path('change/', change, name='change'),
    path('find/', find, name='find'),
    path('', index, name='home'),
    path('view-find/', view_find, name='view_find'),
]

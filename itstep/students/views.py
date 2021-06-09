from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Student

def index(request):
    students_list = Student.objects.all()
    template = loader.get_template('index.html')
    context = {'students':students_list}
    return HttpResponse(template.render(context, request))

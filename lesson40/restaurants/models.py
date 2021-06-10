from django.db import models

# Create your models here.


class Restaurants(models.Model):
    name = models.CharField(max_length=50)
    specialization = models.CharField(max_length=25)
    address = models.CharField(max_length=50)
    web_site = models.CharField(max_length=25, blank=True)
    telephone_number = models.CharField(max_length=25)

from django.db import models

# Create your models here.
class Actor(models.Model):
    first_name = models.CharField(max_lengs=30)
    
from django.db import models
from django.db.models.fields import CharField
from actors.models import Actor


class Genre(models.Model):
    name = CharField(max_length=20)

class Movie(models.Model):
    name = models.CharField(max_length=100)
    year = models.DateField(blank=True)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    actors = models.ManyToManyField(Actor, related_name="movies")
    

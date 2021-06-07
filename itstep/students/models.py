from django.db import models

class Student(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=40)
    grade = models.PositiveIntegerField()
    age = models.PositiveIntegerField()

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"
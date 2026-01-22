from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=150, blank=False)
    age = models.IntegerField(blank=False)
    degree = models.CharField(max_length=100, blank=False)
    email = models.EmailField(max_length=150, unique=True, blank=False)

    def __str__(self):
        return self.name
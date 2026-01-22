from django.db import models

# Create your models here.
class Employee(models.Model):
    name = models.CharField(max_length=100, blank=False)
    skill = models.CharField(max_length=150, blank=False)
    address = models.CharField(max_length=200, blank=False)
    email = models.EmailField(max_length=150, unique=True, blank=False)

    def __str__(self):
        return self.name
from django.db import models

# Create your models here.
class Customer(models.Model):
    """
    Docstring for Customer
    """
    name = models.CharField(max_length=100, null=False)
    address = models.CharField(max_length=200, null=False)
    product = models.CharField(max_length=100)
    email = models.EmailField(max_length=150, unique=True)

    def __str__(self):
        return self.name
    
class Student(models.Model):
    name = models.CharField(max_length=150, null=False)
    roll_no = models.IntegerField(null=False, unique=True)
    father_name = models.CharField(max_length=100, null=False)
    department = models.CharField(max_length=150, null=False)

    def __str__(self):
        return self.name
    
class Employee(models.Model):
    name = models.CharField(max_length=100, null=False)
    age = models.IntegerField(null=False)
    field = models.CharField(max_length=50, null=False)
    role = models.CharField(max_length=100, null=False)

    def __str__(self):
        return self.name
    
class Manager(models.Model):
    name = models.CharField(max_length=100, null=False)
    manage = models.CharField(max_length=100, null=False)
    age = models.IntegerField(null=False)

    def __str__(self):
        return self.name
from django.db import models
from django.contrib.auth.models import User

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
    
class Product(models.Model):
    user = models.ForeignKey(User, default=1, null=True, related_name='products', on_delete=models.CASCADE)
    title = models.CharField(max_length=120)
    content = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=15, decimal_places=2, default=99.99)

    @property
    def sale_price(self):
        return "%.2f" %(float(self.price) * 0.8)
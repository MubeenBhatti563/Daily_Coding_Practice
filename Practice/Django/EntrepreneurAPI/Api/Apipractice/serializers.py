from rest_framework import serializers
from .models import Customer, Student, Employee, Manager

class CustomerSerializer(serializers.ModelSerializer):
    """
    Docstring for CustomerSerializer
    """
    class Meta:
        model = Customer
        fields = "__all__"

class StudentSerializer(serializers.ModelSerializer):
    """
    Docstring for StudentSerializer
    """
    class Meta:
        model = Student
        fields = "__all__"

class EmployeeSerializer(serializers.ModelSerializer):
    """
    Docstring for EmployeeSerializer
    """
    class Meta:
        model = Employee
        fields = "__all__"

class ManagerSerializer(serializers.ModelSerializer):
    """
    Docstring for ManageSeializer
    """
    class Meta:
        model = Manager
        fields = "__all__"
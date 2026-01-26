from rest_framework import serializers
from rest_framework.reverse import reverse
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
    url = serializers.SerializerMethodField(read_only=True)
    email = serializers.EmailField(write_only=True)
    class Meta:
        model = Manager
        fields = [
            "url",
            "email",
            "pk",
            "name",
            "manage",
            "age"
        ]

    def get_url(self, obj):
        request = self.context.get("request")
        if request is None:
            return None
        return reverse("manager-detail", kwargs={"pk": obj.pk}, request=request)
    
    def create(self, validated_data):
        email = validated_data.pop("email", None)
        print(validated_data)
        managaer_instance = Manager.objects.create(**validated_data)
        if email:
            print(f"Sending notification to {email}")
        return managaer_instance
    
    def update(self, instance, validated_data):
        return super().update(instance, validated_data)
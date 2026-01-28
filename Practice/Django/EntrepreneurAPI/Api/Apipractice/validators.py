from rest_framework import serializers
from .models import Manager

def validate_name(attrs):
        qs = Manager.objects.filter(name__iexact=attrs)
        if qs.exists():
            raise serializers.ValidationError(f"{attrs} is already a manager!")
        return attrs

def validate_no_hello(value):
      if "hello" in value.lower():
            raise serializers.ValidationError(f"Hello is not allowed")
      return value
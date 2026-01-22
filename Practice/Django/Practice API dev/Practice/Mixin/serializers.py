from rest_framework import serializers
from .models import Cities

class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Cities
        fields = "__all__"
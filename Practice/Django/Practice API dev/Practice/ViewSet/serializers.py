from rest_framework import serializers
from .models import ViewsetModel

class ViewsetmodelSerializer(serializers.ModelSerializer):
    class Meta:
        model = ViewsetModel
        fields = "__all__"
from rest_framework import serializers

class UsernameSerializer(serializers.Serializer):
    username = serializers.CharField(read_only=True)
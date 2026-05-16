from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Post, Comment, Profile

class PostSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', read_only=True)
    class Meta:
        model = Post
        fields = ['id', 'title', 'content', 'createdAt', 'username']

class CommentSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', read_only=True)
    postname = serializers.CharField(source='post.title', read_only=True)
    class Meta:
        model = Comment
        fields = ['id', 'text', 'createdAt', 'username', 'postname', 'post']
        extra_kwargs = {'post': {'write_only': True}}
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}
    
    def create(self, validated_data):
        user = User(
            username=validated_data['username'],
            email=validated_data['email'],
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
    
class UserProfileSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(required=False)
    username = serializers.CharField(source='user.username', read_only=True)

    class Meta:
        model = Profile
        fields = ['id', 'username', 'name', 'bio', 'image', 'createdAt']
        read_only_fields = ['user', 'createdAt']
from django.shortcuts import get_object_or_404
from rest_framework import viewsets, status
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from .models import Post, Comment
from .serializers import PostSerializer

# Create your views here.
class PostViewSet(viewsets.ViewSet):
    """
    A simple ViewSet for Posts
    """
    queryset = Post.objects.all()

    def list(self, request):
        queryset = self.queryset
        serializer = PostSerializer(queryset, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
    
    def create(self, request):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
    def retrieve(self, request, pk=None):
        try:
            post = get_object_or_404(Post, pk=pk)
            serializer = PostSerializer(post)
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)
    
    def update(self, request, pk=None):
        try:
            post = get_object_or_404(Post, pk=pk)
            serializer = PostSerializer(post)
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
    def destroy(self, request, pk=None):
        try:
            post = get_object_or_404(Post, pk=pk)
            post.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)
    
    def get_permissions(self):
        if self.action == 'list':
            self.permission_classes = [IsAuthenticatedOrReadOnly]
        elif self.action == 'create':
            self.permission_classes = [IsAuthenticated]
        return super().get_permissions()
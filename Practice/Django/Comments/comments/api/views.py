from rest_framework import viewsets, permissions
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer

class PostViewSet(viewsets.ModelViewSet):
    """
    A professional ViewSet for viewing and editing Post instances.
    """
    queryset = Post.objects.all().select_related('user')
    serializer_class = PostSerializer

    def get_permissions(self):
        """
        Custom permissions: 
        - List/Retrieve: Anyone
        - Create/Update/Delete: Authenticated users only
        """
        if self.action in ['list', 'retrieve']:
            return [permissions.IsAuthenticatedOrReadOnly()]
        return [permissions.IsAuthenticated()]

    def perform_create(self, serializer):
        """
        Automatically link the Post to the logged-in user.
        """
        serializer.save(user=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    """
    ViewSet for handling Comment CRUD logic.
    """
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            return [permissions.IsAuthenticatedOrReadOnly()]
        return [permissions.IsAuthenticated()]

    def perform_create(self, serializer):
        # Professional practice: Link comment to current user automatically
        serializer.save(user=self.request.user)
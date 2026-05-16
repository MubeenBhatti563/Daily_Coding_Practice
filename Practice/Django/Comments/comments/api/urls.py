from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import PostViewSet, CommentViewSet, ProfileViewSet

router = DefaultRouter()
router.register(r"posts", PostViewSet, basename='posts')
router.register(r"comments", CommentViewSet, basename='comments')
router.register(r"profile", ProfileViewSet, basename='profile')
urlpatterns = router.urls

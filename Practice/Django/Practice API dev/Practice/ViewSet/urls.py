from .import views
from django.urls import path, include
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("viewset", views.ViewSet, basename='viewset')

urlpatterns = [
    path("", include(router.urls))
]

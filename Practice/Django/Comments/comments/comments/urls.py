from django.contrib import admin
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api_auth/", include("rest_framework.urls")),
    path("api/", include("api.urls")),
    path("api/token/", TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path("api/refresh/token/", TokenRefreshView.as_view(), name='token_refresh')
]

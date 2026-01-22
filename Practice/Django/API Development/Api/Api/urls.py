from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # Web Application endpoint
    path('', include("students.urls")),

    # Api endpoint
    path('api/v1/', include("apiendpoint.urls"))
]

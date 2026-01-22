from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("Api.urls")),
    path("", include("ClassBaseApi.urls")),
    path("", include("Mixin.urls")),
    path("", include("ViewSet.urls"))
]
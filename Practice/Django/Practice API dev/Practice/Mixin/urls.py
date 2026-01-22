from django.urls import path
from . import views

urlpatterns = [
    # path("city", views.CityView.as_view()),
    path("city", views.CityGenericView.as_view()),
    # path("city/<int:pk>", views.CityDetailView.as_view()),
    path("city/<int:pk>", views.CityGenericDetail.as_view())
]

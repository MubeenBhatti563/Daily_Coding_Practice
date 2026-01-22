from django.urls import path
from . import views

urlpatterns = [
    path('', views.student),
    path('student/<int:pk>', views.student_detail)
]
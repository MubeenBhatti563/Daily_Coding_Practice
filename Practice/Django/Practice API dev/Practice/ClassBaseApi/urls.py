from django.urls import path
from . import views

urlpatterns = [
    path('employees/', views.EmployeeView.as_view()),
    path('employees/<int:pk>', views.EmployeeDetail.as_view())
]

from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.home_api),
    path("<int:pk>/", views.get_customer),
    path("student/", views.StudentView.as_view()),
    path("student/<int:pk>/", views.StudentViewSingle.as_view()),
    path("employee/", views.EmployeeView.as_view()),
    path("employee/<int:pk>/", views.EmployeeViewSingle.as_view()),
    path("manager/", views.ManagerView.as_view()),
    path("manager/<int:pk>/", views.ManagerViewSingle.as_view())
]

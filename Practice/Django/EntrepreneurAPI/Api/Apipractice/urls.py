from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from . import views

urlpatterns = [
    path("auth/", obtain_auth_token),
    path("", views.home_api),
    path("<int:pk>/", views.get_customer),
    path("student/", views.StudentView.as_view()),
    path("student/<int:pk>/", views.StudentViewSingle.as_view()),
    path("employee/", views.EmployeeView.as_view()),
    path("employee/<int:pk>/", views.EmployeeViewSingle.as_view()),
    path("manager/", views.ManagerView.as_view()),
    path("manager/<int:pk>/", views.ManagerViewSingle.as_view(), name="manager-detail")
]

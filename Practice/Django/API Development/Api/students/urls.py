from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("employees", views.EmployeeViewSet, basename='employee')

urlpatterns = [
    path("students/", views.students),
    path("students/<int:pk>/", views.student_detail_view),

    # path("employees/", views.Employees.as_view()),
    # path("employees/<int:pk>", views.EmployeesView.as_view()),

    path('', include(router.urls)),
    path('blogs/', views.BlogViews.as_view()),
    path('comments/', views.CommentViews.as_view()),
    path('blogs/<int:pk>', views.BlogDetailView.as_view()),
    path('comments/<int:pk>', views.CommentDetailView.as_view()),
]
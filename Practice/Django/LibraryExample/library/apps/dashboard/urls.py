from django.urls import path
from . import views

app_name = 'dashboard'

urlpatterns = [
    path('', views.dashboard_view, name='dashboard'),
    path('student-info/', views.student_info, name='student_info'),
    path('statistics/', views.statistics, name='statistics'),
    path('borrow-history/', views.borrow_history, name='borrow_history'),
    path('return-book/', views.return_book, name='return_book'),
    path('available-books/', views.available_books, name='available_books'),
]
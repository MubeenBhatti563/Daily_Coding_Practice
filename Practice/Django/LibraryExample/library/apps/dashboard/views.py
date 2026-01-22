"""
Dashboard views with proper authentication and error handling.
"""
import logging
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods
from django.http import Http404

logger = logging.getLogger(__name__)


@login_required(login_url='login')
@require_http_methods(['GET'])
def dashboard_view(request):
    """
    Main dashboard view.
    
    Args:
        request: HTTP request object
        
    Returns:
        Rendered dashboard template
    """
    context = {
        'user': request.user,
    }
    return render(request, 'dashboard/dashboard.html', context)


@login_required(login_url='login')
@require_http_methods(['GET'])
def student_info(request):
    """
    Student information view.
    
    Args:
        request: HTTP request object
        
    Returns:
        Rendered student info template
    """
    context = {
        'user': request.user,
    }
    return render(request, 'dashboard/student_info.html', context)


@login_required(login_url='login')
@require_http_methods(['GET'])
def statistics(request):
    """
    Student statistics view.
    
    Args:
        request: HTTP request object
        
    Returns:
        Rendered statistics template
    """
    context = {
        'user': request.user,
    }
    return render(request, 'dashboard/statistics.html', context)


@login_required(login_url='login')
@require_http_methods(['GET'])
def borrow_history(request):
    """
    Borrow history view.
    
    Args:
        request: HTTP request object
        
    Returns:
        Rendered borrow history template
    """
    context = {
        'user': request.user,
    }
    return render(request, 'dashboard/borrow_history.html', context)


@login_required(login_url='login')
@require_http_methods(['GET', 'POST'])
def return_book(request):
    """
    Book return view.
    
    Args:
        request: HTTP request object
        
    Returns:
        Rendered return book template
    """
    context = {
        'user': request.user,
    }
    return render(request, 'dashboard/return_book.html', context)


@login_required(login_url='login')
@require_http_methods(['GET'])
def available_books(request):
    """
    Available books view.
    
    Args:
        request: HTTP request object
        
    Returns:
        Rendered available books template
    """
    context = {
        'user': request.user,
    }
    return render(request, 'dashboard/available_books.html', context)
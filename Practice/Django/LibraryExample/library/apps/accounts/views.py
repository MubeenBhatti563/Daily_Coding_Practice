"""
User authentication views with proper error handling.
"""
import logging
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_protect
from django.contrib import messages
from .forms import ProfessionalLoginForm, ProfessionalRegisterForm
from utils.constants import (
    SUCCESS_LOGIN, SUCCESS_REGISTER, ERROR_INVALID_CREDENTIALS
)

logger = logging.getLogger(__name__)


def home(request):
    """
    Home page view.
    
    Args:
        request: HTTP request object
        
    Returns:
        Rendered home template
    """
    return render(request, 'base.html')


@require_http_methods(['GET', 'POST'])
@csrf_protect
def login_view(request):
    """
    Handle user login with HTMX support.
    
    Args:
        request: HTTP request object
        
    Returns:
        Rendered login template or redirect on success
    """
    form = ProfessionalLoginForm(request, data=request.POST or None)
    
    if request.method == 'POST':
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            logger.info(f'User {user.username} logged in successfully.')
            
            # HTMX request handling
            if request.headers.get('HX-Request') == 'true':
                response = HttpResponse()
                response['HX-Redirect'] = '/dashboard/'
                return response
            
            messages.success(request, SUCCESS_LOGIN)
            return redirect('dashboard:dashboard')  # Fixed
    
    return render(request, 'accounts/login.html', {'form': form})


@require_http_methods(['GET', 'POST'])
@csrf_protect
def register_view(request):
    """
    Handle user registration with HTMX support.
    
    Args:
        request: HTTP request object
        
    Returns:
        Rendered register template or redirect on success
    """
    form = ProfessionalRegisterForm(request.POST or None)
    
    if request.method == 'POST' and form.is_valid():
        user = form.save()
        logger.info(f'New user registered: {user.username}')
        
        # HTMX request handling
        if request.headers.get('HX-Request') == 'true':
            response = HttpResponse()
            response['HX-Redirect'] = '/login/'
            return response
        
        messages.success(request, SUCCESS_REGISTER)
        return redirect('accounts:login')  # Fixed
    
    return render(request, 'accounts/register.html', {'form': form})


@login_required(login_url='accounts:login')  # Fixed
@require_http_methods(['GET'])
def logout_view(request):
    """
    Handle user logout.
    
    Args:
        request: HTTP request object
        
    Returns:
        Redirect to home page
    """
    username = request.user.username
    logout(request)
    logger.info(f'User {username} logged out.')
    messages.success(request, 'You have been logged out successfully.')
    return redirect('accounts:home')  # Fixed
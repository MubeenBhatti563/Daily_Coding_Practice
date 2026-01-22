"""
Custom decorators for views and functions.
"""
import logging
from functools import wraps
from django.http import JsonResponse
from django.shortcuts import redirect

logger = logging.getLogger(__name__)


def require_ajax(view_func):
    """
    Decorator to require AJAX request.
    Returns 400 Bad Request if not AJAX.
    """
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        if not request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            if request.headers.get('HX-Request') != 'true':
                return JsonResponse({'error': 'AJAX request required'}, status=400)
        return view_func(request, *args, **kwargs)
    return wrapper


def log_action(action_name):
    """
    Decorator to log user actions.
    """
    def decorator(view_func):
        @wraps(view_func)
        def wrapper(request, *args, **kwargs):
            user = request.user.username if request.user.is_authenticated else 'Anonymous'
            logger.info(f'Action: {action_name} | User: {user} | Method: {request.method}')
            return view_func(request, *args, **kwargs)
        return wrapper
    return decorator
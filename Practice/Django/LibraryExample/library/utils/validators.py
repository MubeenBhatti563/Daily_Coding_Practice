"""
Custom validators for forms and models.
"""
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
import re


def validate_username(username):
    """
    Validate username format.
    Only alphanumeric characters and underscores allowed.
    """
    if not re.match(r'^[a-zA-Z0-9_]+$', username):
        raise ValidationError(
            'Username can only contain letters, numbers, and underscores.'
        )


def validate_strong_password(password):
    """
    Validate password strength.
    Must contain uppercase, lowercase, number, and special character.
    """
    if len(password) < 8:
        raise ValidationError('Password must be at least 8 characters long.')
    
    if not re.search(r'[A-Z]', password):
        raise ValidationError('Password must contain uppercase letters.')
    
    if not re.search(r'[a-z]', password):
        raise ValidationError('Password must contain lowercase letters.')
    
    if not re.search(r'\d', password):
        raise ValidationError('Password must contain numbers.')
    
    if not re.search(r'[!@#$%^&*]', password):
        raise ValidationError('Password must contain special characters (!@#$%^&*).')


alphanumeric_validator = RegexValidator(
    regex=r'^[a-zA-Z0-9_-]*$',
    message='Only alphanumeric characters, hyphens, and underscores are allowed.',
)
"""
User authentication and registration forms.
"""
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from utils.validators import validate_username, validate_strong_password
from utils.constants import (
    MIN_PASSWORD_LENGTH, MAX_USERNAME_LENGTH, MAX_EMAIL_LENGTH
)


class ProfessionalLoginForm(AuthenticationForm):
    """
    Enhanced login form with better UX.
    """
    username = forms.CharField(
        label='Username',
        max_length=MAX_USERNAME_LENGTH,
        widget=forms.TextInput(attrs={
            'placeholder': 'Enter your username',
            'class': 'form__input',
            'autocomplete': 'username',
        })
    )
    password = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Enter your password',
            'class': 'form__input',
            'autocomplete': 'current-password',
        })
    )

    def clean(self):
        """Enhanced error handling."""
        super().clean()
        if self.errors:
            self.add_error(None, 'Invalid credentials. Please try again.')


class ProfessionalRegisterForm(UserCreationForm):
    """
    Enhanced registration form with validation.
    """
    email = forms.EmailField(
        label='Email Address',
        max_length=MAX_EMAIL_LENGTH,
        widget=forms.EmailInput(attrs={
            'placeholder': 'Enter your email',
            'class': 'form__input',
            'autocomplete': 'email',
        })
    )
    username = forms.CharField(
        label='Username',
        max_length=MAX_USERNAME_LENGTH,
        validators=[validate_username],
        widget=forms.TextInput(attrs={
            'placeholder': 'Choose a username',
            'class': 'form__input',
            'autocomplete': 'username',
        })
    )
    password1 = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Create a strong password',
            'class': 'form__input',
            'autocomplete': 'new-password',
        }),
        validators=[validate_strong_password],
    )
    password2 = forms.CharField(
        label='Confirm Password',
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Confirm your password',
            'class': 'form__input',
            'autocomplete': 'new-password',
        })
    )

    class Meta:
        model = User
        fields = ('email', 'username', 'password1', 'password2')

    def clean_email(self):
        """Ensure email is unique."""
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('Email already registered.')
        return email

    def clean_username(self):
        """Ensure username is unique."""
        username = self.cleaned_data.get('username')
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError('Username already taken.')
        return username

    def clean_password2(self):
        """Ensure passwords match."""
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError('Passwords do not match.')
        return password2
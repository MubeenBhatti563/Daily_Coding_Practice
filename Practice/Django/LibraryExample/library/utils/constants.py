"""
Application-wide constants.
Centralized configuration for the entire project.
"""

# Application Configuration
APP_NAME = 'Tour Library'
APP_VERSION = '1.0.0'

# Book Status
BOOK_STATUS_CHOICES = {
    'available': 'Available',
    'borrowed': 'Borrowed',
    'reserved': 'Reserved',
    'damaged': 'Damaged',
}

# Borrow Status
BORROW_STATUS_CHOICES = {
    'active': 'Active',
    'returned': 'Returned',
    'overdue': 'Overdue',
}

# Pagination
DEFAULT_PAGE_SIZE = 10
MAX_PAGE_SIZE = 100

# Validation
MIN_PASSWORD_LENGTH = 8
MAX_USERNAME_LENGTH = 150
MAX_EMAIL_LENGTH = 254

# Borrow Rules
DEFAULT_BORROW_DURATION_DAYS = 14
MAX_BOOKS_PER_STUDENT = 5
FINE_PER_DAY = 10  # Currency units

# Error Messages
ERROR_INVALID_CREDENTIALS = 'Invalid username or password.'
ERROR_USER_EXISTS = 'User with this username already exists.'
ERROR_MAX_BOOKS_EXCEEDED = f'Maximum {MAX_BOOKS_PER_STUDENT} books can be borrowed.'
ERROR_NO_BOOKS_AVAILABLE = 'No copies of this book are currently available.'

# Success Messages
SUCCESS_LOGIN = 'Login successful!'
SUCCESS_REGISTER = 'Registration successful! Please log in.'
SUCCESS_BOOK_BORROWED = 'Book borrowed successfully!'
SUCCESS_BOOK_RETURNED = 'Book returned successfully!'
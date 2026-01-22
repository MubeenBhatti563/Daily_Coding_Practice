"""
Book model for library management.
"""
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from utils.constants import BOOK_STATUS_CHOICES


class Book(models.Model):
    """
    Represents a book in the library.
    """
    title = models.CharField(max_length=255, db_index=True)
    author = models.CharField(max_length=255, db_index=True)
    isbn = models.CharField(max_length=13, unique=True)
    description = models.TextField(blank=True)
    category = models.CharField(max_length=100)
    
    publication_date = models.DateField()
    publisher = models.CharField(max_length=255)
    
    total_copies = models.PositiveIntegerField(validators=[MinValueValidator(1)])
    available_copies = models.PositiveIntegerField(validators=[MinValueValidator(0)])
    
    cover_image = models.ImageField(upload_to='book_covers/', blank=True)
    
    status = models.CharField(
        max_length=20,
        choices=BOOK_STATUS_CHOICES.items(),
        default='available'
    )
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Book'
        verbose_name_plural = 'Books'
        indexes = [
            models.Index(fields=['title', 'author']),
            models.Index(fields=['isbn']),
        ]

    def __str__(self):
        return f"{self.title} by {self.author}"
    
    def is_available(self):
        """Check if book has available copies."""
        return self.available_copies > 0
"""
Borrowing transaction model.
"""
from django.db import models
from django.contrib.auth.models import User
from datetime import timedelta
from django.utils import timezone
from utils.constants import (
    BORROW_STATUS_CHOICES,
    DEFAULT_BORROW_DURATION_DAYS
)


class BorrowRecord(models.Model):
    """
    Represents a book borrowing transaction.
    """
    student = models.ForeignKey(User, on_delete=models.CASCADE, related_name='borrows')
    book = models.ForeignKey('books.Book', on_delete=models.CASCADE)
    
    borrow_date = models.DateTimeField(auto_now_add=True)
    due_date = models.DateField()
    return_date = models.DateField(null=True, blank=True)
    
    status = models.CharField(
        max_length=20,
        choices=BORROW_STATUS_CHOICES.items(),
        default='active'
    )
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-borrow_date']
        verbose_name = 'Borrow Record'
        verbose_name_plural = 'Borrow Records'
        indexes = [
            models.Index(fields=['student', 'status']),
            models.Index(fields=['due_date']),
        ]

    def __str__(self):
        return f"{self.student.username} - {self.book.title}"
    
    def save(self, *args, **kwargs):
        """Automatically set due date on creation."""
        if not self.due_date:
            self.due_date = timezone.now().date() + timedelta(days=DEFAULT_BORROW_DURATION_DAYS)
        super().save(*args, **kwargs)
    
    def is_overdue(self):
        """Check if book is overdue."""
        if self.status == 'returned':
            return False
        return timezone.now().date() > self.due_date
    
    def days_until_due(self):
        """Calculate days until due date."""
        if self.status == 'returned':
            return 0
        delta = self.due_date - timezone.now().date()
        return delta.days
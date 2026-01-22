from django.contrib import admin
from .models import Book

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'isbn', 'total_copies', 'available_copies', 'status')
    list_filter = ('status', 'category', 'publication_date')
    search_fields = ('title', 'author', 'isbn')
    readonly_fields = ('created_at', 'updated_at')
    
    fieldsets = (
        ('Book Information', {
            'fields': ('title', 'author', 'isbn', 'description')
        }),
        ('Publication Details', {
            'fields': ('publisher', 'publication_date', 'category')
        }),
        ('Library Information', {
            'fields': ('total_copies', 'available_copies', 'cover_image', 'status')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
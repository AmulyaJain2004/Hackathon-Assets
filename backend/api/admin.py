from django.contrib import admin
from .models import Note


@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    """Admin configuration for the Note model."""
    list_display = ['title', 'owner', 'created_at', 'updated_at']
    list_filter = ['created_at', 'updated_at', 'owner']
    search_fields = ['title', 'content', 'owner__email']
    readonly_fields = ['created_at', 'updated_at']
    fieldsets = (
        (None, {'fields': ('title', 'content', 'owner')}),
        ('Timestamps', {'fields': ('created_at', 'updated_at')}),
    ) 
from django.db import models
from django.conf import settings


class Note(models.Model):
    """
    Note model for storing user notes.
    """
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='notes'
    )

    class Meta:
        ordering = ['-updated_at']

    def __str__(self):
        return self.title 
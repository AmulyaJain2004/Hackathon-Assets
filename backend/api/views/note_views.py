from rest_framework import viewsets, permissions
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend

from api.models import Note
from api.serializers.note_serializers import (
    NoteSerializer,
    NoteDetailSerializer,
    NoteCreateSerializer,
)
from api.permissions import IsOwner


class NoteViewSet(viewsets.ModelViewSet):
    """
    ViewSet for viewing and editing Note instances.
    
    list:
        Return a list of all the notes owned by the authenticated user.
        
    retrieve:
        Return the given note.
        
    create:
        Create a new note.
        
    update:
        Update an existing note.
        
    partial_update:
        Partially update an existing note.
        
    destroy:
        Delete an existing note.
    """
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwner]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['created_at', 'updated_at']
    search_fields = ['title', 'content']
    ordering_fields = ['created_at', 'updated_at', 'title']
    ordering = ['-updated_at']
    
    def get_queryset(self):
        """Return only notes owned by the authenticated user."""
        return self.queryset.filter(owner=self.request.user)
    
    def get_serializer_class(self):
        """Return appropriate serializer class based on the request."""
        if self.action == 'retrieve':
            return NoteDetailSerializer
        elif self.action == 'create':
            return NoteCreateSerializer
        return self.serializer_class 
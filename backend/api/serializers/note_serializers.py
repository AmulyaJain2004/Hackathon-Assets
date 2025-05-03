from rest_framework import serializers
from api.models import Note


class NoteSerializer(serializers.ModelSerializer):
    """Serializer for the Note model."""
    
    class Meta:
        model = Note
        fields = ['id', 'title', 'content', 'created_at', 'updated_at', 'owner']
        read_only_fields = ['id', 'created_at', 'updated_at', 'owner']


class NoteDetailSerializer(serializers.ModelSerializer):
    """Serializer for detailed Note view."""
    
    owner_email = serializers.SerializerMethodField()
    
    class Meta:
        model = Note
        fields = ['id', 'title', 'content', 'created_at', 
                 'updated_at', 'owner', 'owner_email']
        read_only_fields = ['id', 'created_at', 'updated_at', 
                           'owner', 'owner_email']
    
    def get_owner_email(self, obj):
        """Get the email of the note owner."""
        return obj.owner.email


class NoteCreateSerializer(serializers.ModelSerializer):
    """Serializer for creating a Note."""
    
    class Meta:
        model = Note
        fields = ['id', 'title', 'content', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']
    
    def create(self, validated_data):
        """Create a new note."""
        validated_data['owner'] = self.context['request'].user
        return super().create(validated_data) 
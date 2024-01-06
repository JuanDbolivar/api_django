"""serializer"""

from rest_framework import serializers
from .models import Project


class ProjectSerializer(serializers.ModelSerializer):
    """Clase del serializer"""
    class Meta:
        """Define los campos del modelo a serializar"""
        model = Project
        fields = ('id', 'title', 'description', 'technology', 'created_at')
        read_only_fields = ('created_at',)

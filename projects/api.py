"""API"""

from rest_framework import viewsets, permissions
from .serializers import ProjectSerializer
from .models import Project


class ProjectViewset(viewsets.ModelViewSet):
    """Vista para la API del modelo Project"""
    queryset = Project.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = ProjectSerializer

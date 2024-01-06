"""modelos de base de datos"""

from django.db import models


class Project(models.Model):
    """Modelo de tabla para un proyecto"""
    title = models.CharField(max_length=200)
    description = models.TextField()
    technology = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

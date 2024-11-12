from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    # Campos adicionales
    direccion = models.CharField(max_length=255, blank=True, null=True)
    telefono = models.CharField(max_length=20, blank=True, null=True)
    
    # Definición de roles como choices
    class Role(models.TextChoices):
        ADMIN = 'admin', 'Admin'
        CLIENT = 'client', 'Client'
        QUEST = 'quest', 'Quest'

    role = models.CharField(
        max_length=10,
        choices=Role.choices,
        default=Role.QUEST,
    )

    def __str__(self):
        return self.username
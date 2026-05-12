from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser
from sucursales.models import Sucursales

class Usuario(AbstractUser):
    ROL_CHOICES = [
        ('admin', 'Administrador'),
        ('vendedor', 'Vendedor'),
        ('bodeguero', 'Bodeguero'),
        ('contador', 'Contador'),
    ]
    rol = models.CharField(max_length=20, choices=ROL_CHOICES, default='vendedor')
    sucursal= models.ForeignKey(Sucursales, on_delete=models.SET_NULL, null=True, blank=True)
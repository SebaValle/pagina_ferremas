from django.db import models

# Create your models here.
class Cliente(models.Model):
    rut = models.CharField(max_length=12, unique=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    telefono = models.CharField(max_length=15)
    correo = models.EmailField()
    
    def __str__(self):
        return f"{self.nombre} {self.apellido}"
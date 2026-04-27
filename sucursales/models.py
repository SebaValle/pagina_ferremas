from django.db import models

# Create your models here.
class Sucursal(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=250) # Incluye calle, número y ciudad
    telefono = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return self.nombre
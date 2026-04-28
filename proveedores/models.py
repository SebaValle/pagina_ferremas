from django.db import models

# Create your models here.
class Proveedor(models.Model):
    rut_empresa = models.CharField(max_length=12, unique=True)
    nombre_empresa = models.CharField(max_length=100)
    contacto_nombre = models.CharField(max_length=100)
    telefono_contacto = models.CharField(max_length=15)
    

    def __str__(self):
        return self.nombre_empresa
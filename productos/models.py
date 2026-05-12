from django.db import models
from proveedores.models import Proveedor
from sucursales.models import Sucursales 

class Categoria(models.Model):
    nombre = models.CharField(max_length=100)
    def __str__(self): return self.nombre

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE)
    codigo_sku = models.CharField(max_length=50, unique=True, default="N/A")

    def __str__(self):
        return f"{self.nombre} ({self.codigo_sku})"

class InventarioSucursal(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    sucursal = models.ForeignKey(Sucursales, on_delete=models.CASCADE) 
    stock = models.PositiveIntegerField(default=0)
    
    def __str__(self):
        return f"{self.producto.nombre} en {self.sucursal.nombre}"


class DetalleProducto(models.Model): # <--- Asegúrate de que este nombre sea EXACTO
    producto = models.OneToOneField(Producto, on_delete=models.CASCADE, related_name='detalle')
    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    descripcion = models.TextField()

    def __str__(self):
        return f"Detalle de {self.producto.nombre}"
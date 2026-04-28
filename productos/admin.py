from django.contrib import admin

# Register your models here.
from .models import Categoria, Producto, DetalleProducto, InventarioSucursal

admin.site.register(Categoria)
admin.site.register(Producto)
admin.site.register(DetalleProducto)
admin.site.register(InventarioSucursal)
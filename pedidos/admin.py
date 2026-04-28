from django.contrib import admin

# Register your models here.
from .models import Pedido, DetalleVenta, OrdenBodega, Factura

admin.site.register(Pedido)
admin.site.register(DetalleVenta)
admin.site.register(OrdenBodega)
admin.site.register(Factura)
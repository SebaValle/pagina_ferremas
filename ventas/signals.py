from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import DetalleVenta
from productos.models import InventarioSucursal

@receiver(post_save, sender=DetalleVenta)
def descontar_stock(sender, instance, created, **kwargs):
    if created:
        # Buscamos el stock del producto en la sucursal del vendedor
        sucursal_vendedor = instance.venta.vendedor.sucursal
        inventario = InventarioSucursal.objects.get(
            producto=instance.producto, 
            sucursal=sucursal_vendedor
        )
        # Orquestación: Descontamos la cantidad comprada
        inventario.stock -= instance.cantidad
        inventario.save()
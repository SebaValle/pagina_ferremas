from django.db import models

# Create your models here.
from django.db import models
from usuarios.models import Usuario
from clientes.models import Cliente
from productos.models import Producto
from sucursales.models import Sucursales

class Pedido(models.Model):
    ESTADOS = [
        ('pendiente', 'Pendiente'),
        ('preparado', 'Preparado'),
        ('pagado', 'Pagado'),
        ('despachado', 'Despachado'),
        ('entregado', 'Entregado'),
    ]
    ENTREGA = [('despacho', 'Despacho'), ('retiro', 'Retiro')]
    
    fecha = models.DateTimeField(auto_now_add=True)
    total = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    total_usd = models.DecimalField(max_digits=12, decimal_places=2, default=0, help_text="Total convertido")
    valor_dolar_dia = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    tipo_entrega = models.CharField(max_length=20, choices=ENTREGA)
    estado = models.CharField(max_length=20, choices=ESTADOS, default='pendiente')
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    vendedor = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    sucursal = models.ForeignKey(Sucursales, on_delete=models.CASCADE)

class DetalleVenta(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE, related_name='items')
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField()
    precio_unitario_historico = models.DecimalField(max_digits=10, decimal_places=2)
    subtotal = models.DecimalField(max_digits=12, decimal_places=2, default=0)

class OrdenBodega(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    instrucciones = models.TextField(blank=True)
    fecha_emision = models.DateTimeField(auto_now_add=True)

class Factura(models.Model):
    pedido = models.OneToOneField(Pedido, on_delete=models.CASCADE)
    folio = models.CharField(max_length=20, unique=True)
    fecha_emision = models.DateTimeField(auto_now_add=True)
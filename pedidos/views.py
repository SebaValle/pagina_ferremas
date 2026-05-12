from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Pedido, DetalleVenta
from .serializer import PedidoSerializer
from .utils import obtener_valor_dolar
from productos.models import InventarioSucursal
from django.db import transaction

class PedidoViewSet(viewsets.ModelViewSet):
    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer

    @transaction.atomic
    def create(self, request, *args, **kwargs):
        # 1. Obtener valor del dólar (API Externa)
        valor_dolar = obtener_valor_dolar() or 950.0 # Fallback si la API falla
        
        # 2. Lógica de creación del pedido
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        pedido = serializer.save(valor_dolar_dia=valor_dolar)

        total_acumulado = 0
        detalles_data = request.data.get('detalles', [])

        for item in detalles_data:
            # 3. Descontar Stock (Persistencia y lógica interna)
            inv = InventarioSucursal.objects.get(
                producto_id=item['producto'], 
                sucursal=pedido.sucursal
            )
            
            if inv.stock >= item['cantidad']:
                inv.stock -= item['cantidad']
                inv.save()
                
                # Crear detalle
                precio = inv.producto.precio
                sub = precio * item['cantidad']
                DetalleVenta.objects.create(
                    pedido=pedido,
                    producto_id=item['producto'],
                    cantidad=item['cantidad'],
                    precio_unitario=precio,
                    subtotal=sub
                )
                total_acumulado += sub
            else:
                raise Exception(f"No hay stock suficiente para {inv.producto.nombre}")

        # 4. Actualizar totales y conversión
        pedido.total_clp = total_acumulado
        pedido.total_usd = float(total_acumulado) / valor_dolar
        pedido.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)
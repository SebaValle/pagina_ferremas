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
        # 1. API Externa: Obtener dólar
        valor_dolar = obtener_valor_dolar() or 950.0 
        
        # 2. Validar Pedido (Vendedor, Sucursal, Cliente)
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        pedido = serializer.save(valor_dolar_dia=valor_dolar)

        total_acumulado = 0
        # 3. EL FOR: Procesa cada producto del pedido
        items_data = request.data.get('items', [])

        for item in items_data:
            inv = InventarioSucursal.objects.get(
                producto_id=item['producto'], 
                sucursal=pedido.sucursal
            )
            
            if inv.stock >= item['cantidad']:
                inv.stock -= item['cantidad']
                inv.save()
                
                # Obtenemos el precio del producto
                precio_actual = inv.producto.precio
                sub = precio_actual * item['cantidad']
                
                # CORRECCIÓN AQUÍ: Usamos precio_actual en el print
                print(f"DEBUG: Precio encontrado: {precio_actual}") 
                
                # USAR EL NOMBRE EXACTO DEL MODELO
                DetalleVenta.objects.create(
                    pedido=pedido,
                    producto_id=item['producto'],
                    cantidad=item['cantidad'],
                    precio_unitario_historico=precio_actual, 
                    subtotal=sub
                )
                total_acumulado += sub
            else:
                raise Exception(f"No hay stock suficiente para {inv.producto.nombre}")

        # 4. Guardar totales finales en el pedido
        pedido.total_clp = total_acumulado
        pedido.total_usd = float(total_acumulado) / valor_dolar
        pedido.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)
        # 4. Guardar totales finales en el pedido
        pedido.total_clp = total_acumulado
        pedido.total_usd = float(total_acumulado) / valor_dolar
        pedido.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)
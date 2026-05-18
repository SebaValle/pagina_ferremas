from rest_framework import serializers
from .models import Pedido, DetalleVenta

class DetalleVentaSerializer(serializers.ModelSerializer):
    class Meta:
        model = DetalleVenta
        fields = ['producto', 'cantidad', 'precio_unitario_historico', 'subtotal']

class PedidoSerializer(serializers.ModelSerializer):
    # Dejamos que el serializer maneje solo los campos planos del Pedido.
    # Quitamos la línea de 'items = DetalleVentaSerializer(...)' de aquí 
    # para que no interfiera en el método .save() corporativo de DRF.

    class Meta:
        model = Pedido
        fields = '__all__'
        read_only_fields = ['total_clp', 'total_usd', 'valor_dolar_dia']
from rest_framework import serializers
from .models import Pedido, DetalleVenta

class DetalleVentaSerializer(serializers.ModelSerializer):
    class Meta:
        model = DetalleVenta
        # Incluimos todos los campos necesarios
        fields = ['producto', 'cantidad', 'precio_unitario_historico', 'subtotal']
        # Importante: Estos dos los calcula tu vista, no los envía el usuario
        read_only_fields = ['precio_unitario_historico', 'subtotal']

class PedidoSerializer(serializers.ModelSerializer):
    items = DetalleVentaSerializer(many=True)

    class Meta:
        model = Pedido
        fields = [
            'id', 'cliente', 'vendedor', 'sucursal', 
            'tipo_entrega', 'estado', 'total', 
            'total_usd', 'valor_dolar_dia', 'items'
        ]
        # Estos campos los calcularemos nosotros, no el usuario
        read_only_fields = ['total', 'total_usd', 'valor_dolar_dia']

    def create(self, validated_data):
        items_data = validated_data.pop('items')
        pedido = Pedido.objects.create(**validated_data)
        for item in items_data:
            DetalleVenta.objects.create(pedido=pedido, **item)
        return pedido
from rest_framework import serializers
from .models import Pedido, DetalleVenta

class DetalleVentaSerializer(serializers.ModelSerializer):
    class Meta:
        model = DetalleVenta
<<<<<<< HEAD
        fields = ['producto', 'cantidad', 'precio_unitario_historico', 'subtotal']
=======
        # Incluimos todos los campos necesarios
        fields = ['producto', 'cantidad', 'precio_unitario_historico', 'subtotal']
        # Importante: Estos dos los calcula tu vista, no los envía el usuario
        read_only_fields = ['precio_unitario_historico', 'subtotal']
>>>>>>> 62249d084109e205bebea6871b2e3bfd9b9df513

class PedidoSerializer(serializers.ModelSerializer):
    # Dejamos que el serializer maneje solo los campos planos del Pedido.
    # Quitamos la línea de 'items = DetalleVentaSerializer(...)' de aquí 
    # para que no interfiera en el método .save() corporativo de DRF.

    class Meta:
        model = Pedido
        fields = '__all__'
        read_only_fields = ['total_clp', 'total_usd', 'valor_dolar_dia']
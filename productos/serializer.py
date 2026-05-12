from rest_framework import serializers
from .models import Producto, Sucursales, InventarioSucursal, Categoria, DetalleProducto

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'

class ProductoSerializer(serializers.ModelSerializer):
    # Campos calculados para mostrar nombres en lugar de solo IDs
    nombre_categoria = serializers.ReadOnlyField(source='categoria.nombre')
    nombre_proveedor = serializers.ReadOnlyField(source='proveedor.nombre_empresa')

    class Meta:
        model = Producto
        fields = [
            'id', 'nombre', 'marca', 'precio', 'stock', 
            'categoria', 'nombre_categoria', 
            'proveedor', 'nombre_proveedor'
        ]

class SucursalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sucursales 
        fields = '__all__'

class InventarioSerializer(serializers.ModelSerializer):
    producto_nombre = serializers.ReadOnlyField(source='producto.nombre')
    sucursal_nombre = serializers.ReadOnlyField(source='sucursal.nombre')

    class Meta:
        model = InventarioSucursal
        fields = ['id', 'producto', 'producto_nombre', 'sucursal', 'sucursal_nombre', 'stock']

class DetalleProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = DetalleProducto
        fields = '__all__'
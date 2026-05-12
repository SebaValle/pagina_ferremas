from rest_framework import viewsets
# Se agregaron Categoria y DetalleProducto a la importación
from .models import Producto, Sucursales, InventarioSucursal, Categoria, DetalleProducto
from .serializer import (
    ProductoSerializer, SucursalSerializer, InventarioSerializer, 
    CategoriaSerializer, DetalleProductoSerializer
)
from usuarios.models import Usuario 
from usuarios.serializer import UsuarioSerializer

class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer

class SucursalViewSet(viewsets.ModelViewSet):
    queryset = Sucursales.objects.all() 
    serializer_class = SucursalSerializer

class InventarioViewSet(viewsets.ModelViewSet):
    queryset = InventarioSucursal.objects.all()
    serializer_class = InventarioSerializer

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    
class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

class DetalleProductoViewSet(viewsets.ModelViewSet):
    queryset = DetalleProducto.objects.all()
    serializer_class = DetalleProductoSerializer
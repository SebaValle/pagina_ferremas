from rest_framework import viewsets
from .models import Producto, Sucursales, InventarioSucursal
from .serializer import ProductoSerializer, SucursalSerializer, InventarioSerializer
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
class UsuarioViewSet(viewsets.ModelViewSet): # <--- Este nombre debe ser el mismo que importas
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import Producto, InventarioSucursal
from .serializer import ProductoSerializer, InventarioSerializer

class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer

class InventarioViewSet(viewsets.ModelViewSet):
    queryset = InventarioSucursal.objects.all()
    serializer_class = InventarioSerializer
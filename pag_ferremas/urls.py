from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from django.views.generic import TemplateView

# 1. Importaciones limpias (Cada vista desde su propia aplicación)
from clientes.views import ClienteViewSet
from proveedores.views import ProveedorViewSet
from pedidos.views import OrdenBodegaViewSet

# 2. Registro en el Router
router = DefaultRouter()
router.register(r'clientes', ClienteViewSet, basename='clientes')
router.register(r'proveedores', ProveedorViewSet, basename='proveedores') 
router.register(r'ordenes-bodega', OrdenBodegaViewSet, basename='ordenes-bodega')

# 3. Rutas del proyecto (Corregido el prefijo 'api/')
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/gestion', include(router.urls)),       # <-- Corregido: sin la 'c' intrusa
    path('api/', include('productos.urls')),  # Rutas de tu catálogo
    path('', TemplateView.as_view(template_name='login.html'), name='login'),
    path('inicio/', TemplateView.as_view(template_name='index.html'), name='index'), # Raíz limpia
    path('checkout/', TemplateView.as_view(template_name='carrito.html'), name='tienda'), # <-- Cambiado a 'checkout/'
    path('checkout/exito/', TemplateView.as_view(template_name='exito.html'), name='exito'),
    path('panel-vendedor/', TemplateView.as_view(template_name='vistaVendedor.html'), name='panel_vendedor')
]
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductoViewSet, SucursalViewSet, InventarioViewSet, UsuarioViewSet, CategoriaViewSet
from clientes.views import ClienteViewSet
from proveedores.views import ProveedorViewSet
from pedidos.views import PedidoViewSet

router = DefaultRouter()
router.register(r'productos', ProductoViewSet)
router.register(r'categorias', CategoriaViewSet)
router.register(r'sucursales', SucursalViewSet)
router.register(r'inventario', InventarioViewSet)
router.register(r'usuarios', UsuarioViewSet)
router.register(r'clientes', ClienteViewSet)
router.register(r'proveedores', ProveedorViewSet)
router.register(r'pedidos', PedidoViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
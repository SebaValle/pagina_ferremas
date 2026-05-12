from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductoViewSet, SucursalViewSet, InventarioViewSet, UsuarioViewSet 
from pedidos.views import PedidoViewSet

router = DefaultRouter()
router.register(r'lista-productos', ProductoViewSet)
router.register(r'lista-sucursales', SucursalViewSet)
router.register(r'stock-total', InventarioViewSet)
router.register(r'pedidos', PedidoViewSet)
router.register(r'usuarios', UsuarioViewSet) # <-- Asegúrate que NO diga 'usuariosViewSet'

urlpatterns = [
    path('', include(router.urls)),
]
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductoViewSet, InventarioViewSet

router = DefaultRouter()
router.register(r'lista', ProductoViewSet)
router.register(r'stock', InventarioViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
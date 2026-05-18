from rest_framework import viewsets
from .models import Proveedor
from .serializer import ProveedorSerializer


# Create your views here.
from rest_framework import viewsets
from .models import Proveedor
from .serializer import ProveedorSerializer


class ProveedorViewSet(viewsets.ModelViewSet):
    queryset = Proveedor.objects.all()
    serializer_class = ProveedorSerializer
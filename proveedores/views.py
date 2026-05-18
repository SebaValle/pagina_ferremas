from rest_framework import viewsets
from .models import Proveedor
from .serializer import ProveedorSerializer

<<<<<<< HEAD
=======
# Create your views here.
from rest_framework import viewsets
from .models import Proveedor
from .serializer import ProveedorSerializer

>>>>>>> 62249d084109e205bebea6871b2e3bfd9b9df513
class ProveedorViewSet(viewsets.ModelViewSet):
    queryset = Proveedor.objects.all()
    serializer_class = ProveedorSerializer
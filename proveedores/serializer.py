from rest_framework import serializers
from .models import Proveedor

class ProveedorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proveedor
<<<<<<< HEAD
        fields = ['id', 'rut_empresa', 'nombre_empresa', 'contacto_nombre', 'telefono_contacto']
=======
        fields = '__all__'
>>>>>>> 62249d084109e205bebea6871b2e3bfd9b9df513

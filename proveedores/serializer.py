from rest_framework import serializers
from .models import Proveedor

class ProveedorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proveedor

        fields = ['id', 'rut_empresa', 'nombre_empresa', 'contacto_nombre', 'telefono_contacto']

        fields = '__all__'


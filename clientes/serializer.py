from rest_framework import serializers
from .models import Cliente

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente

        fields = '__all__'  # Esto expone todos los campos del cliente (id, nombre, rut, etc.)

        fields = '__all__'


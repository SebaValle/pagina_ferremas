from rest_framework import serializers
from .models import Cliente

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
<<<<<<< HEAD
        fields = '__all__'  # Esto expone todos los campos del cliente (id, nombre, rut, etc.)
=======
        fields = '__all__'
>>>>>>> 62249d084109e205bebea6871b2e3bfd9b9df513

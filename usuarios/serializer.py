from rest_framework import serializers
from .models import Usuario

class UsuarioSerializer(serializers.ModelSerializer):
    # Esto mostrará el nombre de la sucursal en lugar de solo el ID
    nombre_sucursal = serializers.ReadOnlyField(source='sucursal.nombre')
    # Esto mostrará "Vendedor" en lugar de solo "vendedor" (opcional pero se ve mejor)
    rol_display = serializers.CharField(source='get_rol_display', read_only=True)

    class Meta:
        model = Usuario
        fields = [
            'id', 
            'username', 
            'first_name', 
            'last_name', 
            'email', 
            'rol',          # El valor interno ('vendedor')
            'rol_display',  # El valor legible ('Vendedor')
            'sucursal',     # El ID de la sucursal
            'nombre_sucursal', # El nombre de la sucursal
            'is_staff'
        ]
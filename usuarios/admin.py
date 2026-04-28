from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Usuario

# Definimos la configuración personalizada para el panel
class UsuarioAdmin(UserAdmin):
    # Esto organiza tus campos en una sección propia dentro del formulario
    fieldsets = UserAdmin.fieldsets + (
        ('Información de Ferremás', {'fields': ('rol', 'sucursal')}),
    )
    # Esto hace que veas el Rol y la Sucursal en la tabla principal de usuarios
    list_display = ['username', 'email', 'rol', 'sucursal', 'is_staff']

# Registramos el modelo con la configuración personalizada
admin.site.register(Usuario, UsuarioAdmin)
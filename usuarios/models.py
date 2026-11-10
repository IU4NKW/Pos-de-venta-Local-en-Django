from django.db import models
from django.contrib.auth.models import User

class PerfilUsuario(models.Model):
    # Definimos las opciones de roles permitidas en el sistema según el informe
    ROLES = (
        ('administrador', 'Administrador'),
        ('jefe_ventas', 'Jefe de Ventas'),
        ('vendedor', 'Vendedor'),
    )
    
    # Relación uno a uno con el modelo User nativo de Django
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, related_name='perfil')#related name es para poder acceder al perfil desde el usuario, por ejemplo: user.perfil.rol
    
    # Campo para almacenar el rol del usuario
    rol = models.CharField(max_length=30, choices=ROLES, default='vendedor')

    def __str__(self):
        return f"{self.usuario.username} - {self.rol}"
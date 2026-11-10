import os
import django

# Configuramos el entorno de Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LOCAL_POS.settings')
django.setup()

from django.contrib.auth.models import User
from usuarios.models import PerfilUsuario

# Definimos los 3 usuarios de prueba con sus roles
usuarios_prueba = [
    {'username': 'admin_test', 'password': '1234', 'rol': 'administrador'},
    {'username': 'jefe_test', 'password': '1234', 'rol': 'jefe_ventas'},
    {'username': 'vendedor_test', 'password': '1234', 'rol': 'vendedor'},
]

print("--- Creando usuarios de prueba para el POS ---")

for data in usuarios_prueba:
    # Verificamos si el usuario ya existe para no duplicarlo
    user, created = User.objects.get_or_create(username=data['username'])
    if created:
        user.set_password(data['password'])
        user.save()
        print(f"Usuario creado: {data['username']}")
    else:
        print(f"El usuario {data['username']} ya existía.")

    # Creamos o actualizamos su PerfilUsuario asociado
    perfil, perfil_created = PerfilUsuario.objects.get_or_create(usuario=user)
    perfil.rol = data['rol']
    perfil.save()
    print(f"-> Perfil asignado: {data['rol']} para {data['username']}\n")

print("¡Listo! Ya puedes probar iniciar sesión con cualquiera de estos 3 usuarios (clave: 1234).")
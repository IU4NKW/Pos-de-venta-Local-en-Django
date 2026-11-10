from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from .models import PerfilUsuario
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

class CustomLoginView(LoginView): #borrar en produccion
    template_name = 'usuarios/login.html'

    def get_success_url(self):
        user = self.request.user
        
        # Si el usuario no tiene perfil, se crea uno por defecto como 'vendedor' para evitar el error
        perfil, created = PerfilUsuario.objects.get_or_create(
            usuario=user,
            defaults={'rol': 'vendedor'} #borrar en produccion
        )
        
        rol = perfil.rol
        
        if rol == 'administrador':
            return reverse_lazy('dashboard_admin')
        elif rol == 'jefe_ventas':
            return reverse_lazy('dashboard_jefe')
        else:
            return reverse_lazy('pos_venta') 

@login_required
def dashboard_admin(request):
    return render(request, 'usuarios/dashboard_admin.html')

@login_required
def pos_venta(request):
    return render(request, 'usuarios/pos_venta.html')

@login_required
def dashboard_jefe(request):
    return render(request, 'usuarios/dashboard_jefe.html')
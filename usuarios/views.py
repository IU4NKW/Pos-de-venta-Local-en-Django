from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from .models import PerfilUsuario
from django.shortcuts import render, redirect
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


# ---------------------------------------------------------------------------
# Administrador
# ---------------------------------------------------------------------------

@login_required
def admin_pos(request):
    return render(request, 'usuarios/admin_pos.html')

@login_required
def admin_historial(request):
    return render(request, 'usuarios/admin_historial.html')

@login_required
def admin_reportes(request):
    return render(request, 'usuarios/admin_reportes.html')

@login_required
def admin_inventario(request):
    return render(request, 'usuarios/admin_inventario.html')

@login_required
def admin_usuarios(request):
    return render(request, 'usuarios/admin_usuarios.html')

@login_required
def admin_auditoria(request):
    return render(request, 'usuarios/admin_auditoria.html')

@login_required
def abrir_jornada_admin(request):
    return redirect('dashboard_admin')

@login_required
def cerrar_jornada_admin(request):
    return redirect('dashboard_admin')


# ---------------------------------------------------------------------------
# Jefe de ventas
# ---------------------------------------------------------------------------

@login_required
def jefe_pos(request):
    return render(request, 'usuarios/jefe_pos.html')

@login_required
def jefe_historial(request):
    return render(request, 'usuarios/jefe_historial.html')

@login_required
def jefe_arqueo(request):
    return render(request, 'usuarios/jefe_arqueo.html')

@login_required
def jefe_inventario(request):
    return render(request, 'usuarios/jefe_inventario.html')

@login_required
def jefe_alertas(request):
    return render(request, 'usuarios/jefe_alertas.html')

@login_required
def abrir_jornada_jefe(request):
    return redirect('dashboard_jefe')

@login_required
def cerrar_jornada_jefe(request):
    return redirect('dashboard_jefe')


# ---------------------------------------------------------------------------
# Vendedor
# ---------------------------------------------------------------------------

@login_required
def vendedor_historial(request):
    return render(request, 'usuarios/vendedor_historial.html')

@login_required
def vendedor_clientes(request):
    return render(request, 'usuarios/vendedor_clientes.html')

@login_required
def vendedor_devoluciones(request):
    return render(request, 'usuarios/vendedor_devoluciones.html')
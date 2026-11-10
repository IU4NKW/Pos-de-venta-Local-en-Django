from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages
from .models import PerfilUsuario

class CustomLoginView(LoginView):
    template_name = 'usuarios/login.html'

    def get_success_url(self):
        user = self.request.user
        
        try:
            perfil = PerfilUsuario.objects.get(user=user)
            rol = perfil.rol
            
            if rol == 'administrador':
                return reverse_lazy('dashboard_admin')
            elif rol == 'jefe_ventas':
                return reverse_lazy('dashboard_jefe')
            elif rol == 'vendedor':
                return reverse_lazy('pos_venta')
            else:
                messages.error(self.request, 'Tu cuenta tiene un rol inválido o no reconocido.')
                return reverse_lazy('login')
                
        except ObjectDoesNotExist:
            messages.error(self.request, 'error de credenciales')
            return reverse_lazy('login')
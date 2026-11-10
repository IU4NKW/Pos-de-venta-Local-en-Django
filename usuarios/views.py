from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages

class CustomLoginView(LoginView):
    template_name = 'usuarios/login.html'

    def get_success_url(self):
        user = self.request.user
        
        try:
            # Evaluamos directamente contra el PerfilUsuario de negocio
            perfil = user.perfilusuario
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
            # Si el usuario no tiene un perfil de rol asociado
            messages.error(self.request, 'El usuario no tiene un perfil de rol asignado en el sistema.')
            return reverse_lazy('login')
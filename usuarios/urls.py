from django.urls import path
from .views import CustomLoginView
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns = [
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('dashboard/admin/', views.dashboard_admin, name='dashboard_admin'),
    path('dashboard/admin/pos/', views.admin_pos, name='admin_pos'),
    path('dashboard/admin/historial/', views.admin_historial, name='admin_historial'),
    path('dashboard/admin/reportes/', views.admin_reportes, name='admin_reportes'),
    path('dashboard/admin/inventario/', views.admin_inventario, name='admin_inventario'),
    path('dashboard/admin/usuarios/', views.admin_usuarios, name='admin_usuarios'),
    path('dashboard/admin/auditoria/', views.admin_auditoria, name='admin_auditoria'),
    path('dashboard/admin/jornada/abrir/', views.abrir_jornada_admin, name='abrir_jornada_admin'),
    path('dashboard/admin/jornada/cerrar/', views.cerrar_jornada_admin, name='cerrar_jornada_admin'),

    path('dashboard/jefe/', views.dashboard_jefe, name='dashboard_jefe'),
    path('dashboard/jefe/pos/', views.jefe_pos, name='jefe_pos'),
    path('dashboard/jefe/historial/', views.jefe_historial, name='jefe_historial'),
    path('dashboard/jefe/arqueo/', views.jefe_arqueo, name='jefe_arqueo'),
    path('dashboard/jefe/inventario/', views.jefe_inventario, name='jefe_inventario'),
    path('dashboard/jefe/alertas/', views.jefe_alertas, name='jefe_alertas'),
    path('dashboard/jefe/jornada/abrir/', views.abrir_jornada_jefe, name='abrir_jornada_jefe'),
    path('dashboard/jefe/jornada/cerrar/', views.cerrar_jornada_jefe, name='cerrar_jornada_jefe'),

    path('pos/', views.pos_venta, name='pos_venta'),
    path('pos/historial/', views.vendedor_historial, name='vendedor_historial'),
    path('pos/clientes/', views.vendedor_clientes, name='vendedor_clientes'),
    path('pos/devoluciones/', views.vendedor_devoluciones, name='vendedor_devoluciones'),

    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
]


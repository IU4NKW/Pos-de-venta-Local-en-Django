from django.urls import path
from .views import CustomLoginView
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns = [
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('dashboard/admin/', views.dashboard_admin, name='dashboard_admin'),
    path('dashboard/jefe/', views.dashboard_jefe, name='dashboard_jefe'), 
    path('pos/', views.pos_venta, name='pos_venta'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
]


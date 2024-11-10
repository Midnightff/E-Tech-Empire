from django.urls import path
from . import views

urlpatterns = [
    path('proveedores/', views.proveedor_list, name='proveedor_list'),
    path('proveedor/nuevo/', views.proveedor_create, name='proveedor_create'),
    path('proveedor/editar/<int:pk>/', views.proveedor_edit, name='proveedor_edit'),
    path('proveedor/eliminar/<int:pk>/', views.proveedor_delete, name='proveedor_delete'),
]

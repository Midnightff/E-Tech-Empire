from django.urls import path
from . import views

urlpatterns = [
    path('clientes/', views.cliente_list, name='cliente_list'),
    path('cliente/nuevo/', views.cliente_create, name='cliente_create'),
    path('cliente/editar/<int:pk>/', views.cliente_edit, name='cliente_edit'),
    path('cliente/eliminar/<int:pk>/', views.cliente_delete, name='cliente_delete'),
]
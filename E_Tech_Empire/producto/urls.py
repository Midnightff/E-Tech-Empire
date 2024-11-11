from django.urls import path
from . import views

urlpatterns = [
    path('productos/', views.producto_list, name='producto_list'),
    path('producto/nuevo/', views.producto_create, name='producto_create'),
    path('producto/editar/<int:pk>/', views.producto_update, name='producto_update'),
    path('producto/eliminar/<int:pk>/', views.producto_delete, name='producto_delete'),
]

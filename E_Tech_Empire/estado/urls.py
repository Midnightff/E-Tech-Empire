from django.urls import path
from . import views

urlpatterns = [
    path('estados/', views.estado_list, name='estado_list'),
    path('estado/nuevo/', views.estado_create, name='estado_create'),
    path('estado/editar/<int:pk>/', views.estado_edit, name='estado_edit'),
    path('estado/eliminar/<int:pk>/', views.estado_delete, name='estado_delete'),
]
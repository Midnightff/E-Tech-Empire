from django.urls import path
from . import views

urlpatterns = [
    path('marcas/', views.marca_list, name='marca_list'),
    path('marca/nueva/', views.marca_create, name='marca_create'),
    path('marca/editar/<int:pk>/', views.marca_edit, name='marca_edit'),
    path('marca/eliminar/<int:pk>/', views.marca_delete, name='marca_delete'),
]
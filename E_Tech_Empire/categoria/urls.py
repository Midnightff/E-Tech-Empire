
from django.urls import path
from categoria import views

urlpatterns = [
    path('categorias/', views.categoria_list, name='categoria_list'),
    path('categoria/nueva/', views.categoria_create, name='categoria_create'),
    path('categoria/editar/<int:pk>/', views.categoria_update, name='categoria_update'),
    path('categoria/eliminar/<int:pk>/', views.categoria_delete, name='categoria_delete'),
]

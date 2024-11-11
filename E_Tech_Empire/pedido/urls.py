from django.urls import path
from . import views

urlpatterns = [
    path('pedidos/', views.pedido_list, name='pedido_list'),
    path('pedido/nuevo/', views.pedido_create, name='pedido_create'),
    path('pedido/editar/<int:pk>/', views.pedido_edit, name='pedido_edit'),
    path('pedido/eliminar/<int:pk>/', views.pedido_delete, name='pedido_delete'),
]

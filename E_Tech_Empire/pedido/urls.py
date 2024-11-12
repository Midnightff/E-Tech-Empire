from django.urls import path
from . import views

urlpatterns = [
    path('pedidos/', views.lista_pedidos, name='lista_pedidos'),  
    path('pedido/<int:pk>/', views.detalle_pedido, name='detalle_pedido'),  
    path('pedido/crear/', views.crear_pedido, name='crear_pedido'),  
    path('pedido/actualizar/<int:pk>/', views.actualizar_pedido, name='actualizar_pedido'), 
    path('pedido/eliminar/<int:pk>/', views.eliminar_pedido, name='eliminar_pedido'),
    path('api/precio_producto/<int:producto_id>/', views.obtener_precio_producto, name='obtener_precio_producto'),  # Nueva URL para obtener el precio 
]

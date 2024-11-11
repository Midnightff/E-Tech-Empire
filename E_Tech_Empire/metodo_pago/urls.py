from django.urls import path
from . import views

urlpatterns = [
    path('metodos-pago/', views.metodopago_list, name='metodopago_list'),
    path('metodo-pago/nuevo/', views.metodopago_create, name='metodopago_create'),
    path('metodo-pago/editar/<int:pk>/', views.metodopago_edit, name='metodopago_edit'),
    path('metodo-pago/eliminar/<int:pk>/', views.metodopago_delete, name='metodopago_delete'),
]

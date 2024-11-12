from django.db import models
from metodo_pago.models import MetodoPago
from user.models import CustomUser
from estado.models import Estado
from producto.models import Producto
from django.utils import timezone

# Modelo unificado de Pedido y DetallePedido
class Pedido(models.Model):
    codigo = models.CharField(max_length=255, unique=True, null=True, blank=True)
    fecha = models.DateTimeField(auto_now_add=True)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    cliente = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    estado = models.ForeignKey(Estado, on_delete=models.CASCADE)
    metodo_pago = models.ForeignKey(MetodoPago, on_delete=models.CASCADE)
    fecha_pago = models.DateTimeField(default=timezone.now, null=True, blank=True)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE, blank=True, null=True)
    cantidad = models.IntegerField(blank=True, null=True)
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    def __str__(self):
        return f'Pedido {self.id} - Cliente: {self.cliente.nombre} - {self.cantidad} x {self.producto.nombre}'

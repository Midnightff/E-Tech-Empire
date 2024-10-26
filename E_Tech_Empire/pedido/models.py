from django.db import models

from metodo_pago.models import MetodoPago
from cliente.models import Cliente

# Create your models here.
class Pedido(models.Model):
    ESTADOS = [
        ('pendiente', 'Pendiente'),
        ('pagado', 'Pagado'),
        ('cancelado', 'Cancelado'),
        ('enviado', 'Enviado'),
        ('entregado', 'Entregado'),
    ]
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    fecha = models.DateTimeField()
    total = models.DecimalField(max_digits=10, decimal_places=2)
    estado = models.CharField(max_length=10, choices=ESTADOS)
    metodo_pago = models.ForeignKey(MetodoPago, on_delete=models.CASCADE)
    fecha_pago = models.DateTimeField(null=True, blank=True)

    def _str_(self):
        return f'Pedido {self.id} - Cliente: {self.cliente.nombre}'

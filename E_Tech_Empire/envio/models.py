from django.db import models

from pedido.models import Pedido

# Create your models here.
class Envio(models.Model):
    ESTADOS_ENVIO = [
        ('pendiente', 'Pendiente'),
        ('en_camino', 'En camino'),
        ('entregado', 'Entregado'),
        ('cancelado', 'Cancelado'),
    ]
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    fecha_envio = models.DateTimeField()
    fecha_entrega_estimada = models.DateField()
    estado = models.CharField(max_length=10, choices=ESTADOS_ENVIO)
    direccion_entrega = models.TextField()

    def _str_(self):
        return f'Envío de Pedido {self.pedido.id}'

from django.db import models

from pedido.models import Pedido
from estado.models import Estado

# Create your models here.
class Envio(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    fecha_envio = models.DateTimeField()
    fecha_entrega_estimada = models.DateField()
    estado = models.ForeignKey(Estado, on_delete=models.CASCADE)
    direccion_entrega = models.TextField()

    def _str_(self):
        return f'Envío de Pedido {self.pedido.id}'

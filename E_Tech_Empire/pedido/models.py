from django.db import models

from metodo_pago.models import MetodoPago
from user.models import CustomUser
from estado.models import Estado

# Create your models here.
class Pedido(models.Model):
    codigo = models.CharField(max_length=255, unique=True, null=True, blank=True)
    fecha = models.DateTimeField()
    total = models.DecimalField(max_digits=10, decimal_places=2)
    cliente = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    estado = models.ForeignKey(Estado, on_delete=models.CASCADE)
    metodo_pago = models.ForeignKey(MetodoPago, on_delete=models.CASCADE)
    fecha_pago = models.DateTimeField(null=True, blank=True)


    def _str_(self):
        return f'Pedido {self.id} - Cliente: {self.cliente.nombre}'

from django import forms
from django.utils import timezone
from .models import Pedido, Producto

class PedidoForm(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = ['cliente', 'estado', 'metodo_pago', 'producto', 'cantidad', 'precio_unitario', 'total']
        exclude = ['codigo', 'fecha', 'fecha_pago']  # Eliminamos 'fecha_pago' de los campos visibles
        widgets = {
            'cliente': forms.Select(attrs={'class': 'form-control'}),
            'estado': forms.Select(attrs={'class': 'form-control'}),
            'metodo_pago': forms.Select(attrs={'class': 'form-control'}),
            'producto': forms.Select(attrs={'class': 'form-control', 'id': 'id_producto'}),
            'cantidad': forms.NumberInput(attrs={'class': 'form-control', 'id': 'id_cantidad'}),
            'precio_unitario': forms.NumberInput(attrs={'class': 'form-control', 'id': 'id_precio_unitario', 'readonly': 'readonly'}),
            'total': forms.NumberInput(attrs={'class': 'form-control', 'id': 'id_total', 'readonly': 'readonly'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if not self.instance.pk:  
            self.instance.fecha_pago = timezone.now()



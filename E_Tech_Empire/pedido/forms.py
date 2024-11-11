from django import forms
from .models import Pedido
from metodo_pago.models import MetodoPago
from estado.models import Estado
from user.models import CustomUser

class PedidoForm(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = ['codigo', 'fecha', 'total', 'cliente', 'estado', 'metodo_pago', 'fecha_pago']
        widgets = {
            'fecha': forms.DateTimeInput(attrs={'type': 'datetime-local', 'class': 'form-control'}),
            'total': forms.NumberInput(attrs={'class': 'form-control'}),
            'codigo': forms.TextInput(attrs={'class': 'form-control'}),
            'cliente': forms.Select(attrs={'class': 'form-control'}),
            'estado': forms.Select(attrs={'class': 'form-control'}),
            'metodo_pago': forms.Select(attrs={'class': 'form-control'}),
            'fecha_pago': forms.DateTimeInput(attrs={'type': 'datetime-local', 'class': 'form-control'}),
        }

    def clean_codigo(self):
        codigo = self.cleaned_data.get('codigo')
        if not codigo:
            raise forms.ValidationError("El código del pedido es obligatorio.")
        return codigo

    def clean_total(self):
        total = self.cleaned_data.get('total')
        if total <= 0:
            raise forms.ValidationError("El total debe ser mayor a 0.")
        return total

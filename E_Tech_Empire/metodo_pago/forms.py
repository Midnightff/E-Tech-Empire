from django import forms
from .models import MetodoPago

class MetodoPagoForm(forms.ModelForm):
    class Meta:
        model = MetodoPago
        fields = ['nombre']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre del método de pago'}),
        }

    def clean_nombre(self):
        nombre = self.cleaned_data.get('nombre')
        
        # Validación de unicidad
        if MetodoPago.objects.filter(nombre=nombre).exists():
            raise forms.ValidationError("Ya existe un método de pago con este nombre.")
        
        return nombre
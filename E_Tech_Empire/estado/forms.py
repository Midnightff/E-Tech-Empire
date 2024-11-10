
# estado/forms.py

from django import forms
from .models import Estado

class EstadoForm(forms.ModelForm):
    class Meta:
        model = Estado
        fields = ['nombre']  # Incluimos el campo del modelo
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre del estado', 'required': 'required'}),
        }

    def clean_nombre(self):
        nombre = self.cleaned_data.get('nombre')

        # Validación de unicidad del nombre (además de la configuración en el modelo)
        if Estado.objects.filter(nombre=nombre).exists():
            raise forms.ValidationError("Ya existe un estado con este nombre.")
        
        return nombre



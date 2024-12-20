from django import forms
from .models import Marca

class MarcaForm(forms.ModelForm):
    class Meta:
        model = Marca
        fields = ['nombre']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el nombre de la marca', 'required': 'required'})
        }

    def clean_nombre(self):
        nombre = self.cleaned_data.get('nombre')
        

       
        if not nombre:
            raise forms.ValidationError("El nombre de la marca no puede estar vacío.")
        
       
        if Marca.objects.filter(nombre=nombre).exists():
            raise forms.ValidationError("Ya existe una marca con este nombre.")
        
        return nombre


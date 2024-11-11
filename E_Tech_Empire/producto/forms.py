from django import forms
from .models import Producto

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'descripcion', 'imagen', 'precio', 'stock', 'categoria', 'marca', 'proveedor']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control'}),
            'imagen': forms.FileInput(attrs={'class': 'form-control'}),
            'precio': forms.NumberInput(attrs={'class': 'form-control'}),
            'stock': forms.NumberInput(attrs={'class': 'form-control'}),
            'categoria': forms.Select(attrs={'class': 'form-control', 'id': 'categoriaSelect', 'name': 'categoria', 'required': 'required'}),
            'marca': forms.Select(attrs={'class': 'form-control', 'id': 'marcaSelect', 'name': 'marca', 'required': 'required'}),
            'proveedor': forms.Select(attrs={'class': 'form-control', 'id': 'proveedorSelect', 'name': 'proveedor', 'required': 'required'}),
        }

from django import forms
from .models import Proveedor

class ProveedorForm(forms.ModelForm):
    class Meta:
        model = Proveedor
        fields = ['nombre', 'direccion', 'telefono', 'email']  # Incluimos los campos del modelo

    def clean_telefono(self):
        telefono = self.cleaned_data.get('telefono')

        # Validación: Asegurarse de que el teléfono solo tenga números
        if not telefono.isdigit():
            raise forms.ValidationError("El teléfono solo debe contener números.")
        
        # Validación adicional de longitud si se necesita
        if len(telefono) < 10:
            raise forms.ValidationError("El teléfono debe tener al menos 10 caracteres.")
        
        return telefono

    def clean_email(self):
        email = self.cleaned_data.get('email')

        # Validación de unicidad del email (ya es única en el modelo, pero agregamos la validación adicional)
        if Proveedor.objects.filter(email=email).exists():
            raise forms.ValidationError("Ya existe un proveedor con este correo electrónico.")
        
        return email



from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .forms import ProveedorForm
from .models import Proveedor

# Vista para listar todos los proveedores
def proveedor_list(request):
    proveedores = Proveedor.objects.all()  # Obtiene todos los proveedores
    return render(request, 'proveedor/proveedor_list.html', {'proveedores': proveedores})

# Vista para crear un nuevo proveedor
def proveedor_create(request):
    if request.method == 'POST':
        form = ProveedorForm(request.POST)
        if form.is_valid():
            form.save()  # Guarda el nuevo proveedor
            messages.success(request, "Proveedor creado correctamente.")
            return redirect('proveedor_list')  # Redirige a la lista de proveedores
        else:
            messages.error(request, "Hubo un error al crear el proveedor. Verifica los datos.")
    else:
        form = ProveedorForm()
    return render(request, 'proveedor/proveedor_form.html', {'form': form, 'title': 'Crear Proveedor'})

# Vista para editar un proveedor existente
def proveedor_edit(request, pk):
    proveedor = get_object_or_404(Proveedor, pk=pk)
    if request.method == 'POST':
        form = ProveedorForm(request.POST, instance=proveedor)
        if form.is_valid():
            form.save()  # Guarda los cambios
            messages.success(request, "Proveedor editado correctamente.")
            return redirect('proveedor_list')
        else:
            messages.error(request, "Hubo un error al editar el proveedor. Verifica los datos.")
    else:
        form = ProveedorForm(instance=proveedor)  # Cargar el formulario con los datos del proveedor
    return render(request, 'proveedor/proveedor_form.html', {'form': form, 'title': 'Editar Proveedor'})

# Vista para eliminar un proveedor
def proveedor_delete(request, pk):
    proveedor = get_object_or_404(Proveedor, pk=pk)
    if request.method == 'POST':
        proveedor.delete()
        messages.success(request, "Proveedor eliminado correctamente.")
        return redirect('proveedor_list')
    return render(request, 'proveedor/proveedor_confirm_delete.html', {'proveedor': proveedor})

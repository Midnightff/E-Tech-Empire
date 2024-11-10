

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .forms import MarcaForm
from .models import Marca

def marca_list(request):
    marcas = Marca.objects.all()  # Obtiene todas las marcas
    return render(request, 'marca/marca_list.html', {'marcas': marcas})

def marca_create(request):
    if request.method == 'POST':
        form = MarcaForm(request.POST)
        if form.is_valid():
            form.save()  # Guarda la nueva marca
            messages.success(request, "Marca creada correctamente.")
            return redirect('marca_list')  # Redirige a la lista de marcas
        else:
            messages.error(request, "Hubo un error al crear la marca. Verifica los datos.")
    else:
        form = MarcaForm()
    return render(request, 'marca/marca_form.html', {'form': form, 'title': 'Crear Marca'})

def marca_edit(request, pk):
    marca = get_object_or_404(Marca, pk=pk)
    if request.method == 'POST':
        form = MarcaForm(request.POST, instance=marca)
        if form.is_valid():
            form.save()  # Guarda los cambios
            messages.success(request, "Marca editada correctamente.")
            return redirect('marca_list')
        else:
            messages.error(request, "Hubo un error al editar la marca. Verifica los datos.")
    else:
        form = MarcaForm(instance=marca)
    return render(request, 'marca/marca_form.html', {'form': form, 'title': 'Editar Marca'})

def marca_delete(request, pk):
    marca = get_object_or_404(Marca, pk=pk)
    if request.method == 'POST':
        marca.delete()
        messages.success(request, "Marca eliminada correctamente.")
        return redirect('marca_list')
    return render(request, 'marca/marca_confirm_delete.html', {'marca': marca})

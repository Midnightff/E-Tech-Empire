

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .forms import EstadoForm
from .models import Estado

def estado_list(request):
    estados = Estado.objects.all()  # Obtiene todos los estados
    return render(request, 'estado_list.html', {'estados': estados})

def estado_create(request):
    if request.method == 'POST':
        form = EstadoForm(request.POST)
        if form.is_valid():
            form.save()  # Guarda el nuevo estado
            messages.success(request, "Estado creado correctamente.")
            return redirect('estado_list')  # Redirige a la lista de estados
        else:
            messages.error(request, "Hubo un error al crear el estado. Verifica los datos.")
    else:
        form = EstadoForm()
    return render(request, 'estado_form.html', {'form': form, 'title': 'Crear Estado'})

def estado_edit(request, pk):
    estado = get_object_or_404(Estado, pk=pk)
    if request.method == 'POST':
        form = EstadoForm(request.POST, instance=estado)
        if form.is_valid():
            form.save()  # Guarda los cambios
            messages.success(request, "Estado editado correctamente.")
            return redirect('estado_list')
        else:
            messages.error(request, "Hubo un error al editar el estado. Verifica los datos.")
    else:
        form = EstadoForm(instance=estado)
    return render(request, 'estado_form.html', {'form': form, 'title': 'Editar Estado'})

def estado_delete(request, pk):
    estado = get_object_or_404(Estado, pk=pk)
    if request.method == 'POST':
        estado.delete()
        messages.success(request, "Estado eliminado correctamente.")
        return redirect('estado_list')
    messages.error(request, 'Error al eliminar el estado.')


from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .forms import ClienteForm
from .models import Cliente

def cliente_list(request):
    clientes = Cliente.objects.all()
    return render(request, 'cliente/cliente_list.html', {'clientes': clientes})

def cliente_create(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Cliente creado correctamente.")
            return redirect('cliente_list')
        else:
            messages.error(request, "Error al crear el cliente. Verifica los datos.")
    else:
        form = ClienteForm()
    return render(request, 'cliente/cliente_form.html', {'form': form, 'title': 'Crear Cliente'})

def cliente_edit(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    if request.method == 'POST':
        form = ClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
            messages.success(request, "Cliente editado correctamente.")
            return redirect('cliente_list')
        else:
            messages.error(request, "Error al editar el cliente. Verifica los datos.")
    else:
        form = ClienteForm(instance=cliente)
    return render(request, 'cliente/cliente_form.html', {'form': form, 'title': 'Editar Cliente'})

def cliente_delete(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    if request.method == 'POST':
        cliente.delete()
        messages.success(request, "Cliente eliminado correctamente.")
        return redirect('cliente_list')
    return render(request, 'cliente/cliente_confirm_delete.html', {'cliente': cliente})
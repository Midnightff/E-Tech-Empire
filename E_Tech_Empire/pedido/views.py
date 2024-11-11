from uuid import uuid4
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.contrib import messages
from .models import Pedido
from .forms import PedidoForm

# Vista para la lista de pedidos
def pedido_list(request):
    pedidos = Pedido.objects.all()
    return render(request, 'pedido_list.html', {'pedidos': pedidos})

def pedido_create(request):
    if request.method == 'POST':
        form = PedidoForm(request.POST)
        if form.is_valid():
            pedido = form.save(commit=False)
            # Genera un código único
            pedido.codigo = str(uuid4.uuid4())[:8].upper()  # Código de 8 caracteres
            pedido.save()
            messages.success(request, 'Pedido creado correctamente.')
            return redirect('pedido_list')
        else:
            messages.error(request, 'Hubo un error al crear el pedido.')
    else:
        form = PedidoForm()
    return render(request, 'pedido_form.html', {'form': form})

# Vista para editar un pedido
def pedido_edit(request, pk):
    pedido = get_object_or_404(Pedido, pk=pk)
    if request.method == 'POST':
        form = PedidoForm(request.POST, instance=pedido)
        if form.is_valid():
            form.save()
            messages.success(request, 'Pedido actualizado correctamente.')
            return redirect('pedido_list')
        else:
            messages.error(request, 'Hubo un error al actualizar el pedido.')
    else:
        form = PedidoForm(instance=pedido)
    return render(request, 'pedido_form.html', {'form': form})

# Vista para eliminar un pedido
def pedido_delete(request, pk):
    pedido = get_object_or_404(Pedido, pk=pk)
    if request.method == 'POST':
        pedido.delete()
        messages.success(request, 'Pedido eliminado correctamente.')
        return redirect('pedido_list')
    messages.error(request, 'Hubo un error al eliminar el pedido.')

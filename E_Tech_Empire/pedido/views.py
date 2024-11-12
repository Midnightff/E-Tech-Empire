import uuid
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.http import JsonResponse
from .models import Pedido, Producto
from .forms import PedidoForm

def lista_pedidos(request):
    pedidos = Pedido.objects.all()
    return render(request, 'pedido_list.html', {'pedidos': pedidos})

def detalle_pedido(request, pk):
    pedido = get_object_or_404(Pedido, pk=pk)
    return render(request, 'detalle_pedido.html', {'pedido': pedido})

def crear_pedido(request):
    if request.method == 'POST':
        form = PedidoForm(request.POST)
        if form.is_valid():
            pedido = form.save(commit=False)
            pedido.codigo = str(uuid.uuid4())  # Genera un código único para el pedido
            pedido.save()
            messages.success(request, 'Pedido creado exitosamente.')
            return redirect('lista_pedidos')
    else:
        form = PedidoForm()
    
    productos = Producto.objects.all()  # Obtén la lista de productos
    return render(request, 'pedido_form.html', {'form': form, 'productos': productos})  # Envía los productos al contexto

def actualizar_pedido(request, pk):
    pedido = get_object_or_404(Pedido, pk=pk)
    if request.method == 'POST':
        form = PedidoForm(request.POST, instance=pedido)
        if form.is_valid():
            form.save()
            messages.success(request, 'Pedido actualizado exitosamente.')
            return redirect('lista_pedidos')
    else:
        form = PedidoForm(instance=pedido)
    
    productos = Producto.objects.all()  # Obtén la lista de productos
    return render(request, 'pedido_form.html', {'form': form, 'productos': productos})  # Envía los productos al contexto

def eliminar_pedido(request, pk):
    pedido = get_object_or_404(Pedido, pk=pk)
    if request.method == 'POST':
        pedido.delete()
        messages.success(request, 'Pedido eliminado exitosamente.')
        return redirect('lista_pedidos')
    messages.error(request, 'No se pudo eliminar el pedido.')

def obtener_precio_producto(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    return JsonResponse({'precio': producto.precio})  # Asegúrate de que 'precio' sea el campo correcto en tu modelo

import json
import uuid
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from user.decorators import superuser_required
from .models import Pedido, Producto
from .forms import PedidoForm

@superuser_required
@login_required
def lista_pedidos(request):
    pedidos = Pedido.objects.all()
    return render(request, 'pedido_list.html', {'pedidos': pedidos})

@superuser_required
@login_required
def detalle_pedido(request, pk):
    pedido = get_object_or_404(Pedido, pk=pk)
    return render(request, 'detalle_pedido.html', {'pedido': pedido})

@superuser_required
@login_required
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

@superuser_required
@login_required
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

@superuser_required
@login_required
def eliminar_pedido(request, pk):
    pedido = get_object_or_404(Pedido, pk=pk)
    if request.method == 'POST':
        pedido.delete()
        messages.success(request, 'Pedido eliminado exitosamente.')
        return redirect('lista_pedidos')
    messages.error(request, 'No se pudo eliminar el pedido.')


def obtener_precio_producto(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    return JsonResponse({'precio': producto.precio}) 



@csrf_exempt
@login_required
def crear_pedido_api(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        producto_id = data.get('producto_id')
        
        if request.user.is_authenticated:  # Verificar si el usuario está logueado
            try:
                producto = Producto.objects.get(id=producto_id)
                Pedido.objects.create(
                    codigo=str(uuid.uuid4()),
                    producto=producto,
                    cantidad=1,
                    precio_unitario=producto.precio,
                    cliente=request.user,
                    fecha=timezone.now(),
                    fecha_pago=timezone.now(),
                    estado_id=3,
                    total=producto.precio*1,
                    metodo_pago_id=1
                )
                return JsonResponse({'exito': True, 'mensaje': 'Pedido creado exitosamente.'}) 
            except Producto.DoesNotExist:
                return JsonResponse({'exito': False, 'error': 'Producto no encontrado'})
        else:
            return JsonResponse({'exito': False, 'error': 'Usuario no autenticado'})  

    return JsonResponse({'exito': False, 'error': 'Método no permitido'})
# producto/views.py

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Producto
from .forms import ProductoForm
from django.http import JsonResponse
from user.decorators import superuser_required
from django.contrib.auth.decorators import login_required

@superuser_required
@login_required 
def producto_list(request):
    productos = Producto.objects.all()
    return render(request, 'producto_list.html', {'productos': productos, 'title': 'Listado de Productos'})

@superuser_required
@login_required 
def producto_create(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST, request.FILES)
        if not form.is_valid():
            messages.error(request, "Error al guardar la imagen. Asegúrate de que el archivo sea una imagen válida.")
        if form.is_valid():
            form.save()
            messages.success(request, "Producto creado correctamente.")
            return redirect('producto_list')
        else:
            messages.error(request, "Error al crear el producto. Verifica los datos.")
    else:
        form = ProductoForm()
    return render(request, 'producto_form.html', {'form': form, 'title': 'Crear Producto'})

@superuser_required
@login_required 
def producto_update(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    if request.method == 'POST':
        form = ProductoForm(request.POST, request.FILES, instance=producto)
        if form.is_valid():
            form.save()
            messages.success(request, "Producto actualizado correctamente.")
            return redirect('producto_list')
        else:
            messages.error(request, "Error al actualizar el producto.")
    else:
        form = ProductoForm(instance=producto)
    return render(request, 'producto_form.html', {'form': form, 'title': 'Editar Producto'})

@superuser_required
@login_required 
def producto_delete(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    if request.method == 'POST':
        producto.delete()
        messages.success(request, "Producto eliminado correctamente.")
        return redirect('producto_list')
    messages.error(request, 'Error al eliminar el producto.')


def productos_cliente(request):
    productos = Producto.objects.all()
    productos_data = [
        {
            'id': producto.id,
            'nombre': producto.nombre,
            'precio': producto.precio,
            'descripcion': producto.descripcion,
            'imagen': producto.imagen.url if producto.imagen else None,
        } 
        for producto in productos
    ]
    return JsonResponse({'productos': productos_data})

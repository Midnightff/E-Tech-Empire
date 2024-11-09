from django.shortcuts import render, redirect, get_object_or_404
from .models import Categoria
from .forms import CategoriaForm
from django.contrib import messages

# Create your views here.

def categoria_list(request):
    categorias = Categoria.objects.all()
    return render(request, 'categoria_list.html', {'categorias': categorias})


def categoria_create(request):
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Categoría guardada correctamente.')
            return redirect('categoria_list')
        else:
            messages.error(request, 'Error al guardar la categoría.')
    else:
        form = CategoriaForm()
    return render(request, 'categoria_form.html', {'form': form, 'title': 'Crear Categoría'})


def categoria_update(request, pk):
    categoria = get_object_or_404(Categoria, pk=pk)
    if request.method == 'POST':
        form = CategoriaForm(request.POST, instance=categoria)
        if form.is_valid():
            form.save()
            messages.success(request, 'Categoría editada correctamente.')
            return redirect('categoria_list')
        else:
            messages.error(request, 'Error al editar la categoría.')
    else:
        form = CategoriaForm(instance=categoria)
    return render(request, 'categoria_form.html', {'form': form, 'title': 'Editar Categoría'})

def categoria_delete(request, pk):
    categoria = get_object_or_404(Categoria, pk=pk)
    if request.method == 'POST':
        categoria.delete()
        messages.success(request, 'Categoría eliminada correctamente.')
        return redirect('categoria_list')
    messages.error(request, 'Error al eliminar la categoría.')

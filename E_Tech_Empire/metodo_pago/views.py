from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .forms import MetodoPagoForm
from .models import MetodoPago
from user.decorators import superuser_required
from django.contrib.auth.decorators import login_required

@superuser_required
@login_required
def metodopago_list(request):
    metodos_pago = MetodoPago.objects.all()
    return render(request, 'metodopago_list.html', {'metodos_pago': metodos_pago})

@superuser_required
@login_required
def metodopago_create(request):
    if request.method == 'POST':
        form = MetodoPagoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Método de pago creado correctamente.")
            return redirect('metodopago_list')
        else:
            messages.error(request, "Error al crear el método de pago. Verifica los datos.")
    else:
        form = MetodoPagoForm()
    return render(request, 'metodopago_form.html', {'form': form, 'title': 'Crear Método de Pago'})

@superuser_required
@login_required
def metodopago_edit(request, pk):
    metodopago = get_object_or_404(MetodoPago, pk=pk)
    if request.method == 'POST':
        form = MetodoPagoForm(request.POST, instance=metodopago)
        if form.is_valid():
            form.save()
            messages.success(request, "Método de pago editado correctamente.")
            return redirect('metodopago_list')
        else:
            messages.error(request, "Error al editar el método de pago. Verifica los datos.")
    else:
        form = MetodoPagoForm(instance=metodopago)
    return render(request, 'metodopago_form.html', {'form': form, 'title': 'Editar Método de Pago'})


@superuser_required
@login_required
def metodopago_delete(request, pk):
    metodopago = get_object_or_404(MetodoPago, pk=pk)
    if request.method == 'POST':
        metodopago.delete()
        messages.success(request, "Método de pago eliminado correctamente.")
        return redirect('metodopago_list')
    messages.error(request, "Error al eliminar el método de pago.")

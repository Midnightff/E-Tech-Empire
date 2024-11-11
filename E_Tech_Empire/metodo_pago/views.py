from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .forms import MetodoPagoForm
from .models import MetodoPago

def metodopago_list(request):
    metodos_pago = MetodoPago.objects.all()
    return render(request, 'metodopago/metodopago_list.html', {'metodos_pago': metodos_pago})

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
    return render(request, 'metodopago/metodopago_form.html', {'form': form, 'title': 'Crear Método de Pago'})

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
    return render(request, 'metodopago/metodopago_form.html', {'form': form, 'title': 'Editar Método de Pago'})

def metodopago_delete(request, pk):
    metodopago = get_object_or_404(MetodoPago, pk=pk)
    if request.method == 'POST':
        metodopago.delete()
        messages.success(request, "Método de pago eliminado correctamente.")
        return redirect('metodopago_list')
    return render(request, 'metodopago/metodopago_confirm_delete.html', {'metodopago': metodopago})

from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import RegistroForm, SimpleLoginForm

def registro(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')  # Redirige a la página de inicio u otra página
    else:
        form = RegistroForm()
    return render(request, 'registration/registro.html', {'form': form})

def login_view(request):
    print("login_view llamada")  # Mensaje de depuración
    if request.method == 'POST':
        print(request.POST)  # Ver datos enviados
        form = SimpleLoginForm(request.POST)  # Usar el formulario básico
        print("Verificando si el formulario es válido")  # Mensaje de depuración
        if form.is_valid():
            # Autenticar al usuario
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            print(f"Intentando autenticar: {username}")  # Mensaje de depuración
            if user is not None:
                print("Autenticación exitosa")  # Mensaje de depuración
                login(request, user)
                if user.is_superuser:
                    return redirect('dashboard')
                else:
                    return redirect('index')
            else:
                print("Autenticación fallida")  # Mensaje de depuración
                form.add_error(None, "Usuario o contraseña incorrectos")
        else:
            print("Errores del formulario:", form.errors)  # Mensaje de depuración para ver errores del formulario
    else:
        form = SimpleLoginForm()  # Usar el formulario básico

    return render(request, 'registration/login.html', {'form': form})
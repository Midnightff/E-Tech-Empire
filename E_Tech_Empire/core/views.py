from django.http import JsonResponse
from django.shortcuts import render
from user.decorators import superuser_required
from django.contrib.auth.decorators import login_required
# Create your views here.
@superuser_required
def dashboard(request):
    return render(request, 'admin/dashboard.html')

def index(request):
    return render(request, 'client/index.html')

@login_required
def carrito(request):
    return render(request, 'client/carrito.html')

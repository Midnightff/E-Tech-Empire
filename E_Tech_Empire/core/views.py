from django.shortcuts import render

# Create your views here.
def dashboard(request):
    return render(request, 'admin/dashboard.html')

def index(request):
    return render(request, 'client/index.html')
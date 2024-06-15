from django.shortcuts import render
from .models import Servicio
from .forms import ServicioForm

# Create your views here.
def index(request):
    context={}
    return render(request, 'servicios/index.html', context)

def nservicios(request):
    servicios = Servicio.objects.all()
    context = {'servicios': servicios}
    return render(request, 'servicios/nservicios.html', context)
from django.shortcuts import render
from data.models import Titulo, Proyecto

# Create your views here.
def index(request):
    return render(request, 'core/index.html', {
        'titulos':Titulo.objects.all(),
        'proyectos':Proyecto.objects.all(),
    })
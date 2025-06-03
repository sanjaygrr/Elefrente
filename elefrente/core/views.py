from django.shortcuts import render
from core.models import Recurso, MiembroEquipo

# Create your views here.

def home(request):
    return render(request, 'core/home.html')

def recursos(request):
    recursos = Recurso.objects.select_related('nivel', 'categoria').all()
    return render(request, 'core/recursos.html', {'recursos': recursos})

def quienes_somos(request):
    equipo = MiembroEquipo.objects.all()
    return render(request, 'core/quienes_somos.html', {'equipo': equipo})

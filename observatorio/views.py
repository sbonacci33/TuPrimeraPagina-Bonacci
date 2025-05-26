from django.shortcuts import render, redirect
from .models import Informe, Categoria, ConsultaUsuario
from .forms import InformeForm
from django.contrib import messages


def home(request):
    return render(request, 'observatorio/home.html')

def crear_informe(request):
    if request.method == 'POST':
        form = InformeForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, '✅ Informe guardado con éxito.')
            return redirect('crear_informe')  # Redirige a la misma vista
    else:
        form = InformeForm()
    return render(request, 'observatorio/crear_informe.html', {'form': form})

def listar_informes(request):
    informes = Informe.objects.all().order_by('-fecha')
    return render(request, 'observatorio/listar_informes.html', {'informes': informes})

def buscar_informes(request):
    resultados = []
    termino = ""
    if request.method == 'GET':
        termino = request.GET.get('termino', '')
        if termino:
            resultados = Informe.objects.filter(titulo__icontains=termino)

            # Guardamos la búsqueda
            ConsultaUsuario.objects.create(termino_buscado=termino)

    return render(request, 'observatorio/buscar.html', {'resultados': resultados, 'termino': termino})


from django.shortcuts import render, redirect, get_object_or_404
from .models import Informe, Categoria, ConsultaUsuario
from .forms import InformeForm, SuscriptorForm
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
            from django.db.models import Q
            resultados = Informe.objects.filter(
                Q(titulo__icontains=termino) |
                Q(resumen__icontains=termino)
            )


            # Guardamos la búsqueda
            ConsultaUsuario.objects.create(termino_buscado=termino)

    return render(request, 'observatorio/buscar.html', {'resultados': resultados, 'termino': termino})

def suscribirse(request):
    if request.method == 'POST':
        form = SuscriptorForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "✅ ¡Te suscribiste con éxito!")
            return redirect('home')
    else:
        form = SuscriptorForm()
    return render(request, 'observatorio/suscribirse.html', {'form': form})

def detalle_informe(request, informe_id):
    informe = get_object_or_404(Informe, id=informe_id)
    return render(request, 'observatorio/detalle_informe.html', {'informe': informe})

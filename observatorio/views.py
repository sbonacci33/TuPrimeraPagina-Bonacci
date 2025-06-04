from django.shortcuts import render, redirect, get_object_or_404
from .models import Informe, Categoria, ConsultaUsuario
from .forms import InformeForm, SuscriptorForm, RegistroUsuarioForm
from django.contrib import messages
from django.db.models import Q
from django.contrib.auth import login as auth_login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView


def home(request):
    return render(request, 'observatorio/home.html')


def about(request):
    """Muestra información general del sitio."""
    return render(request, 'observatorio/about.html')

@login_required(login_url='login')
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

@login_required(login_url='login')
def listar_informes(request):
    informes = Informe.objects.all().order_by('-fecha')
    return render(request, 'observatorio/listar_informes.html', {'informes': informes})

def buscar_informes(request):
    resultados = []
    termino = ""
    if request.method == 'GET':
        termino = request.GET.get('termino', '')
        if termino:
            resultados = Informe.objects.filter(
                Q(titulo__icontains=termino) |
                Q(resumen__icontains=termino) |
                Q(autor__icontains=termino)
            )


            # Guarda la búsqueda
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

@login_required(login_url='login')
def detalle_informe(request, informe_id):
    informe = get_object_or_404(Informe, id=informe_id)
    return render(request, 'observatorio/detalle_informe.html', {'informe': informe})

@login_required(login_url='login')
def editar_informe(request, informe_id):
    informe = get_object_or_404(Informe, id=informe_id)
    if request.method == 'POST':
        form = InformeForm(request.POST, instance=informe)
        if form.is_valid():
            form.save()
            messages.success(request, '✅ Informe actualizado con éxito.')
            return redirect('detalle_informe', informe_id=informe.id)
    else:
        form = InformeForm(instance=informe)
    return render(request, 'observatorio/editar_informe.html', {'form': form, 'informe': informe})


@login_required(login_url='login')
def eliminar_informe(request, informe_id):
    informe = get_object_or_404(Informe, id=informe_id)
    if request.method == 'POST':
        informe.delete()
        messages.success(request, '✅ Informe eliminado.')
        return redirect('listar_informes')
    return render(request, 'observatorio/eliminar_informe.html', {'informe': informe})


class UsuarioLoginView(LoginView):
    template_name = 'observatorio/login.html'


class UsuarioLogoutView(LogoutView):
    next_page = 'home'


def registro_usuario(request):
    if request.method == 'POST':
        form = RegistroUsuarioForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('listar_informes')
    else:
        form = RegistroUsuarioForm()
    return render(request, 'observatorio/registro.html', {'form': form})

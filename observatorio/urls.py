from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('crear/', views.crear_informe, name='crear_informe'),
    path('informes/', views.listar_informes, name='listar_informes'),
    path('buscar/', views.buscar_informes, name='buscar_informes'),
    path('suscribirse/', views.suscribirse, name='suscribirse'),
    path('informe/<int:informe_id>/', views.detalle_informe, name='detalle_informe'),
]

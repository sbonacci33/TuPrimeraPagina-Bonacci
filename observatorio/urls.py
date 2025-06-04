from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('crear/', views.crear_informe, name='crear_informe'),
    path('informes/', views.listar_informes, name='listar_informes'),
    path('buscar/', views.buscar_informes, name='buscar_informes'),
    path('suscribirse/', views.suscribirse, name='suscribirse'),
    path('informe/<int:informe_id>/', views.detalle_informe, name='detalle_informe'),
    path('informe/<int:informe_id>/editar/', views.editar_informe, name='editar_informe'),
    path('informe/<int:informe_id>/eliminar/', views.eliminar_informe, name='eliminar_informe'),
    path('login/', views.UsuarioLoginView.as_view(), name='login'),
    path('logout/', views.logout_usuario, name='logout_usuario'),
    path('registro/', views.registro_usuario, name='registro_usuario'),
]

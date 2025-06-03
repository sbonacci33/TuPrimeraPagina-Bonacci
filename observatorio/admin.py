from django.contrib import admin

from .models import Categoria, Informe, ConsultaUsuario, Suscriptor

admin.site.register(Categoria)
admin.site.register(Informe)
admin.site.register(ConsultaUsuario)
admin.site.register(Suscriptor)

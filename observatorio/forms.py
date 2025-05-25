from django import forms
from .models import Categoria, Informe, ConsultaUsuario

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = '__all__'

class InformeForm(forms.ModelForm):
    class Meta:
        model = Informe
        fields = '__all__'

class ConsultaUsuarioForm(forms.ModelForm):
    class Meta:
        model = ConsultaUsuario
        fields = '__all__'

from django import forms
from .models import Categoria, Informe, ConsultaUsuario, Suscriptor

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = '__all__'

class InformeForm(forms.ModelForm):
    class Meta:
        model = Informe
        fields = ['titulo', 'resumen', 'contenido', 'categoria', 'autor']
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Título del informe'}),
            'resumen': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Resumen del contenido', 'rows': 3}),
            'contenido': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Texto completo del informe', 'rows': 8}),
            'categoria': forms.Select(attrs={'class': 'form-select'}),
            'autor': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Autor/a del informe'}),
        }


class SuscriptorForm(forms.ModelForm):
    class Meta:
        model = Suscriptor
        fields = ['nombre', 'apellido', 'email']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre'}),
            'apellido': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Apellido'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Correo electrónico'}),
        }
        error_messages = {
            'email': {
                'invalid': 'Ingresá una dirección de correo válida.',
                'unique': 'Este correo ya está registrado.',
            },
        }


class ConsultaUsuarioForm(forms.ModelForm):
    class Meta:
        model = ConsultaUsuario
        fields = '__all__'



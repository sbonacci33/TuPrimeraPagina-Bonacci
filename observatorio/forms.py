from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Categoria, Informe, ConsultaUsuario, Suscriptor, Perfil

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


class RegistroUsuarioForm(UserCreationForm):
    first_name = forms.CharField(label='Nombre', max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(label='Apellido', max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'form-control'}))
    dni = forms.CharField(label='DNI', max_length=20, widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'dni', 'email', 'password1', 'password2']

    def save(self, commit=True):
        user = super().save(commit)
        dni = self.cleaned_data['dni']
        Perfil.objects.create(user=user, dni=dni)
        return user



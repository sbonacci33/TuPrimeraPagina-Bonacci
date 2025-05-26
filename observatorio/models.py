from django.db import models

class Categoria(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    
    def __str__(self):
        return self.nombre
    
class Informe(models.Model):
    titulo = models.CharField(max_length=200)
    resumen = models.TextField()
    contenido = models.TextField()
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    fecha = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.titulo

class ConsultaUsuario(models.Model):
    termino_buscado = models.CharField(max_length=100)
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.termino_buscado

from django.db import models

# Create your models here.
from django.db import models
class Libro(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.CharField(max_length=100)
    genero = models.CharField(max_length=50)
    fecha_publicacion = models.DateField()
    def _str_(self):
        return self.titulo
    
class Usuario(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    def _str_(self):
        return self.nombre
    
class Prestamo(models.Model):
    codigof = models.ForeignKey(Libro, on_delete=models.CASCADE)
    cedulaf = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    fecha_prestamo = models.DateField(auto_now_add=True)
    fecha_devolucion = models.DateField(null=True, blank=True)

    def str(self):
        return f"{self.libro.titulo} - {self.usuario.nombre}"
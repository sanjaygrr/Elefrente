from django.db import models

# Create your models here.

class Nivel(models.Model):
    nombre = models.CharField(max_length=10)  # Ejemplo: A1, A2, B1, B2

    def __str__(self):
        return self.nombre

class Categoria(models.Model):
    nombre = models.CharField(max_length=50)  # Ejemplo: Gramática, Vocabulario, Canciones

    def __str__(self):
        return self.nombre

class Recurso(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField()
    nivel = models.ForeignKey(Nivel, on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    enlace = models.URLField(blank=True, null=True)  # Para videos, artículos, etc.

    def __str__(self):
        return self.titulo

class MiembroEquipo(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    foto = models.ImageField(upload_to='equipo/', blank=True, null=True)
    red_social = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.nombre

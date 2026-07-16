from django.db import models

class Artista(models.Model):
    nombre = models.CharField(max_length=200)
    biografia = models.TextField(blank=True)
    genero_musical = models.CharField(max_length=100)
    fecha_formacion = models.DateField()

    def __str__(self):
        return self.nombre


class Album(models.Model):
    artista = models.ForeignKey(Artista, related_name='albumes', on_delete=models.CASCADE)
    titulo = models.CharField(max_length=200)
    fecha_lanzamiento = models.DateField()
    numero_canciones = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.titulo} - {self.artista.nombre}"
    
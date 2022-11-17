from django.db import models

# Create your models here.

class Pelicula(models.Model):

    titulo= models.CharField(max_length=60)
    genero = models.CharField(max_length=30)
    director = models.CharField(max_length=60)
    fecha_estreno = models.DateField()
    presupuesto = models.IntegerField()


class Actor(models.Model):

    nombre_apellido = models.CharField(max_length=70)
    origen = models.CharField(max_length=40)
    edad = models.IntegerField()


class Serie(models.Model):

    titulo = models.CharField(max_length=70)
    genero = models.CharField(max_length=30)
    temporadas = models.IntegerField()
    fecha_estreno = models.DateField()
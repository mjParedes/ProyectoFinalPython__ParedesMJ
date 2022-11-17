from django.http import HttpResponse
from mainAPP.models import *

def Saludo(request):
    return HttpResponse('''
    <h1>Bienvenidos a MovieFy</h1>
    <h3>Conoce TODO de tus peliculas favoritas</h3>
    ''')


def ShowMovie(request):

    # pelicula = Pelicula.objects.all()
    def mostrar():
        data = Pelicula.objects.all()
        
    
    mensaje = f"Titulo:  || Genero:"

    return HttpResponse(mensaje)
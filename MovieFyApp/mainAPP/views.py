from django.shortcuts import render
from mainAPP.models import *
from mainAPP.forms import *

# Create your views here.

def inicio(request):
    return render(request, "mainAPP/index.html")


def peliculas(request):
    return render(request, "mainAPP/peliculas.html")

def creacion_pelicula(request):
    
    if request.method == "POST":
        titulo_p = request.POST["titulo"]
        genero_p = request.POST["genero"]
        director_p = request.POST["director"]
        fecha_estreno_p = request.POST["fecha_estreno"]
        presupuesto_p = request.POST["presupuesto"]

        pelicula = Pelicula(titulo=titulo_p, genero=genero_p, director=director_p,fecha_estreno=fecha_estreno_p,presupuesto=presupuesto_p)
        pelicula.save()
    
    return render(request, "mainAPP/peliculas_formulario.html")



def series(request):
    return render(request, "mainAPP/series.html")

def creacion_serie(request):
    
    if request.method == "POST":
        titulo_s = request.POST["titulo"]
        genero_s = request.POST["genero"]
        temporadas_s = request.POST["temporadas"]
        fecha_estreno_s = request.POST["fecha_estreno"]

        serie = Serie(titulo=titulo_s, genero=genero_s,fecha_estreno=fecha_estreno_s,temporadas=temporadas_s)
        serie.save()
    
    return render(request, "mainAPP/series_formulario.html")



def actores(request):
    return render(request, "mainAPP/actores.html")

def creacion_actores(request):

    if request.method == "POST":
        nombre_apellido = request.POST["nombre_apellido"]
        origen = request.POST["origen"]
        edad = request.POST["edad"]
    
        actor = Actor(nombre_apellido=nombre_apellido, origen=origen,edad=edad)
        actor.save()
    
    return render(request, "mainAPP/actores_formulario.html")


def buscar_actores(request):
    
    if request.GET:
        nombre_actor= request.GET.get("nombre_actor","")
        
        if nombre_actor == "":
            lista_actores= []
        else:
            lista_actores = Actor.objects.filter(nombre_apellido__icontains=nombre_actor)
        return render(request,"mainAPP/busqueda_actores.html",{"listado_actores":lista_actores})
    
    return render(request, "mainAPP/busqueda_actores.html",{"listado_actores":[]})


# def peliculaFormulario(request):
#     return render(request, "mainAPP/peliculas-formulario.html" )

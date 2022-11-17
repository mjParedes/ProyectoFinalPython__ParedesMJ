from django.urls import path
from mainAPP.views import *


urlpatterns = [
    path("inicio/", inicio, name="moviefy-inicio"),

    path("peliculas/", peliculas, name="moviefy-peliculas"),
    path("peliculas/crear/", creacion_pelicula, name="moviefy-peliculas-crear"),
   
    path("series/", series, name="moviefy-series"),
    path("series/crear/", creacion_serie, name="moviefy-series-crear"),

    path("actores/", actores, name="moviefy-actores"),
    path("actores/crear/", creacion_actores, name="moviefy-actores-crear"),
    path("actores/buscar/", buscar_actores, name="moviefy-actores-buscar"),


]
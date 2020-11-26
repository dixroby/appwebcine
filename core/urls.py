from django.urls import path
from .views import *

app_name = 'pelicula'
urlpatterns = [
    path('', home, name="home"),
    path('galeria/', galeria, name="galeria"),
    path('listado-peliculas',listado_pelicula,name="listado_pelicula"),
    path('nueva-pelicula',nueva_pelicula,name="nueva_pelicula"),
    path('modificar-pelicula/<id>/',modificar_pelicula,name="modificar-pelicula"),
    path('eliminar-pelicula/<id>/',eliminar_pelicula,name="eliminar_pelicula"),
    path('registro/',RegistroUsuario.as_view(),name="registro"),
]

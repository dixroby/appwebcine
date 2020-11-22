from django.shortcuts import render, redirect
from .models import Pelicula
from .forms import PeliculaForm

def home(request):

    return render(request, 'core/home.html')

def galeria(request) :

    return render(request,'core/galeria.html')

def listado_pelicula(request):
    pelicula = Pelicula.objects.all()
    data = {"peliculas":pelicula}
    return render(request,'core/listado_peliculas.html',data)


def nueva_pelicula(request):
    data = {
        'form': PeliculaForm()
    }
    if request.method == 'POST':
        formulario = PeliculaForm(request.POST) 
        if formulario.is_valid():
            formulario.save()
            data['mensaje'] = 'Pelicula Registrada'


    return render(request,'core/nueva_pelicula.html',data)

def modificar_pelicula(request,id):
    pelicula = Pelicula.objects.get(id = id)
    data = {
        'form': PeliculaForm(instance = pelicula)
    }
    if request.method == 'POST':
        formulario = PeliculaForm(data = request.POST, instance = pelicula) 
        if formulario.is_valid():
            formulario.save()
            data['mensaje'] = 'Pelicula modificado con éxito'
            data['form'] = formulario


    return render(request,'core/modificar_pelicula.html',data)

def eliminar_pelicula(request,id):
    pelicula = Pelicula.objects.get(id = id)
    pelicula.delete()

    return redirect(to = "listado_pelicula")


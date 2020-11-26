from django.shortcuts import render, redirect
from .models import *
from .forms import PeliculaForm, CustomUserForm
from django.contrib.auth.decorators import login_required, permission_required
from django.views.generic import View

from django.contrib.auth import login, authenticate
def listado_clase (request) :
    data = {
        "peliculas":Clase.objects.all()
    }
    return render(request, 'core/home.html',data)

def home(request):
    data = {
        "peliculas":Pelicula.objects.all()
    }
    return render(request, 'core/home.html',data)

def galeria(request) :    
    return render(request,'core/galeria.html')

def listado_pelicula(request):
    pelicula = Pelicula.objects.all()
    data = {"peliculas":pelicula}
    return render(request,'core/listado_peliculas.html',data)

@permission_required('core.add_pelicula')
def nueva_pelicula(request):
    data = {
        'form': PeliculaForm()
    }
    if request.method == 'POST':
        formulario = PeliculaForm(request.POST, files = request.FILES) 
        if formulario.is_valid():
            formulario.save()
            data['mensaje'] = 'Pelicula Registrada'
        data['form'] = formulario


    return render(request,'core/nueva_pelicula.html',data)

def modificar_pelicula(request,id):
    pelicula = Pelicula.objects.get(id = id)
    data = {
        'form': PeliculaForm(instance = pelicula)
    }
    if request.method == 'POST':
        formulario = PeliculaForm(data = request.POST, instance = pelicula, files = request.FILES) 
        if formulario.is_valid():
            formulario.save()
            data['mensaje'] = 'Pelicula modificado con éxito'
        data['form'] = PeliculaForm(instance = Pelicula.objects.get(id = id)) 


    return render(request,'core/modificar_pelicula.html',data)

def eliminar_pelicula(request,id):
    pelicula = Pelicula.objects.get(id = id)
    pelicula.delete()

    return redirect(to = "listado_pelicula")

class RegistroUsuario(View):
    http_method_names = ['get','post']
    teplate_name = 'registration/registrar.html'

    def get (self , request) :
        data = {
        'form':CustomUserForm
        }
        return render(request,self.teplate_name,data)

    def post (self, request ):
        formulario = CustomUserForm(request.POST)
        if formulario.is_valid():
            formulario.save() 
            #autenticar al usuario  y redirigir a /
            username = formulario.cleaned_data["username"]
            password = formulario.cleaned_data["password1"]
            user = authenticate(username = username,password= password)
            login(request,user)
            return redirect("pelicula:home")

        
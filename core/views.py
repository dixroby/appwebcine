from django.shortcuts import render

def home(request):

    return render(request, 'core/home.html')

def galeria(request) :

    return render(request,'core/galeria.html')
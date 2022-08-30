from django.shortcuts import render
from django.http import HttpResponse
from .models import  Paises, Jugadores, Estadios, Partidos

# Create your views here.
def inicio(request):
    return render(request,"AppMundial/inicio.html")

def paises(request):
    return render(request,"AppMundial/paises.html")

def jugadores(request):
    return render(request,"AppMundial/jugadores.html")

def estadios(request):
    return render(request,"AppMundial/estadios.html")

def partidos (request):
    return render(request,"AppMundial/partidos.html")
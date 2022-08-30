from django.shortcuts import render
from django.http import HttpResponse
from .models import  Paises, Jugadores, Estadios, Partidos
from AppMundial.forms import PaisesFormulario, JugadoresFormulario, EstadiosFormulario, PartidosFormulario

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

'''
PAIS
'''
def paisesFormulario(request):
    if request.method =='POST':
        miFormulario=PaisesFormulario(request.POST)
        if miFormulario.is_valid:
            info=miFormulario.cleaned_data
            nombre=info.get("nombre")
            continente=info.get("continente")
            grupo=info.get("grupo")
            pais = Paises(nombre=nombre, continente=continente, grupo=grupo)
            pais.save()
            return render(request,"AppMundial/inicio.html",{"mensaje": "Pais creado"})
        else:
            return render(request,"AppMundial/inicio.html",{"mensaje": "ERROR"})

    else:
        miFormulario=PaisesFormulario()
        return render(request,"AppMundial/paisesFormulario.html",{"formulario":miFormulario})
    return render(request,"AppMundial/paisesFormulario.html")

'''
JUGADOR
'''
def jugadoresFormulario(request):
    if request.method =='POST':
        miFormulario=JugadoresFormulario(request.POST)
        if miFormulario.is_valid:
            info=miFormulario.cleaned_data
            nombre=info.get("nombre")
            apellido=info.get("apellido")
            edad=info.get("edad")
            pais=info.get("edad")
            equipo=info.get("equipo")
            jugador = Jugadores(nombre=nombre, apellido=apellido, edad=edad, pais=pais, equipo=equipo)
            jugador.save()
            return render(request,"AppMundial/inicio.html",{"mensaje": "Jugador creado"})
        else:
            return render(request,"AppMundial/inicio.html",{"mensaje": "ERROR"})

    else:
        miFormulario=JugadoresFormulario()
        return render(request,"AppMundial/jugadoresFormulario.html",{"formulario":miFormulario})
    return render(request,"AppMundial/jugadoresFormulario.html")

'''
ESTADIO
'''
def estadiosFormulario(request):
    if request.method =='POST':
        miFormulario=EstadiosFormulario(request.POST)
        if miFormulario.is_valid:
            info=miFormulario.cleaned_data
            nombre=info.get("nombre")
            capacidad=info.get("capacidad")
            estadio = Estadios(nombre=nombre, capacidad=capacidad)
            estadio.save()
            return render(request,"AppMundial/inicio.html",{"mensaje": "Estadio creado"})
        else:
            return render(request,"AppMundial/inicio.html",{"mensaje": "ERROR"})

    else:
        miFormulario=EstadiosFormulario()
        return render(request,"AppMundial/estadiosFormulario.html",{"formulario":miFormulario})
    return render(request,"AppMundial/estadiosFormulario.html")

'''
PARTIDOS
'''
def partidosFormulario(request):
    if request.method =='POST':
        miFormulario=PartidosFormulario(request.POST)
        if miFormulario.is_valid:
            info=miFormulario.cleaned_data
            instancia=info.get("instancia")
            pais1=info.get("pais1")
            pais2=info.get("pais2")
            resultado=info.get("resultado")
            partido = Partidos(instancia=instancia, pais1=pais1, pais2=pais2, resultado=resultado)
            partido.save()
            return render(request,"AppMundial/inicio.html",{"mensaje": "Pais creado"})
        else:
            return render(request,"AppMundial/inicio.html",{"mensaje": "ERROR"})

    else:
        miFormulario=PartidosFormulario()
        return render(request,"AppMundial/partidosFormulario.html",{"formulario":miFormulario})
    return render(request,"AppMundial/partidosFormulario.html")
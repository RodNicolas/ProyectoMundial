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
        if miFormulario.is_valid():
            info=miFormulario.cleaned_data
            nombre=info.get("nombre")
            continente=info.get("continente")
            grupo=info.get("grupo")
            pais = Paises(nombre=nombre, continente=continente, grupo=grupo)
            pais.save()
            return render(request,"AppMundial/paisesFormulario.html",{"mensaje": "Pais creado, puede crear otro","formulario":miFormulario,"pais":pais.nombre})
        else:
            return render(request,"AppMundial/paisesFormulario.html",{"mensaje": "ERROR","formulario":miFormulario})

    else:
        miFormulario=PaisesFormulario()
        return render(request,"AppMundial/paisesFormulario.html",{"formulario":miFormulario})
    return render(request,"AppMundial/paisesFormulario.html")

def busquedaPxC (request):
    return render(request,"AppMundial/busquedaPxC.html")

def buscar2 (request):
    
    if request.GET['continente']:
        cont=request.GET['continente']
        paises=Paises.objects.filter(continente=cont)
        if len(paises)!=0:
            return render(request,"AppMundial/busquedaPxC.html",{"paises":paises,"cont":cont})
        else:
            mensajenohay="No se encontraron datos para esta solicitud"
            return render(request,"AppMundial/busquedaPxC.html",{"noencontrado":mensajenohay})
    else:
        respuesta="No enviaste datos"
    return render(request, "AppMundial/busquedaPxC.html",{"respuesta":respuesta})

def busquedaPxG (request):
    return render(request,"AppMundial/busquedaPxG.html")

def buscar3 (request):
    
    if request.GET['grupo']:
        grup=request.GET['grupo']
        paises=Paises.objects.filter(grupo=grup)
        if len(paises)!=0:
            return render(request,"AppMundial/busquedaPxG.html",{"paises":paises,"grupo":grup})
        else:
            mensajenohay="No se encontraron datos para esta solicitud"
            return render(request,"AppMundial/busquedaPxG.html",{"noencontrado":mensajenohay})
    else:
        respuesta="No enviaste datos"
    return render(request, "AppMundial/busquedaPxG.html",{"respuesta":respuesta})
'''
JUGADOR
'''
def jugadoresFormulario(request):
    if request.method =='POST':
        miFormulario=JugadoresFormulario(request.POST)
        if miFormulario.is_valid():
            info=miFormulario.cleaned_data
            nombre=info.get("nombre")
            apellido=info.get("apellido")
            edad=info.get("edad")
            pais=info.get("pais")
            equipo=info.get("equipo")
            jugador = Jugadores(nombre=nombre, apellido=apellido, edad=edad, pais=pais, equipo=equipo)
            jugador.save()
            return render(request,"AppMundial/jugadoresFormulario.html",{"mensaje": "Jugador creado, puede crear otro","formulario":miFormulario,"jugador":jugador.apellido})
        else:
            return render(request,"AppMundial/jugadoresFormulario.html",{"mensaje": "ERROR","formulario":miFormulario})

    else:
        miFormulario=JugadoresFormulario()
        return render(request,"AppMundial/jugadoresFormulario.html",{"formulario":miFormulario})
    return render(request,"AppMundial/jugadoresFormulario.html")

def busquedaJxP (request):
    return render(request,"AppMundial/busquedaJxP.html")

def buscar (request):
    
    if request.GET['pais']:
        nacionalidad=request.GET['pais']
        jugadores=Jugadores.objects.filter(pais=nacionalidad)
        if len(jugadores)!=0:
            return render(request,"AppMundial/busquedaJxP.html",{"jugadores":jugadores,"nacionalidad":nacionalidad})
        else:
            mensajenohay="No se encontraron datos para esta solicitud"
            return render(request,"AppMundial/busquedaJxP.html",{"noencontrado":mensajenohay})
    else:

        respuesta="No enviaste datos"
    return render(request, "AppMundial/busquedaJxP.html",{"respuesta":respuesta})

def busquedaJxE (request):
    return render(request,"AppMundial/busquedaJxE.html")

def buscar4 (request):
    
    if request.GET['equipo']:
        team=request.GET['equipo']
        jugadores=Jugadores.objects.filter(equipo=team)
        if len(jugadores)!=0:
            return render(request,"AppMundial/busquedaJxE.html",{"jugadores":jugadores,"equipo":team})
        else:
            mensajenohay="No se encontraron datos para esta solicitud"
            return render(request,"AppMundial/busquedaJxE.html",{"noencontrado":mensajenohay})
    else:

        respuesta="No enviaste datos"
    return render(request, "AppMundial/busquedaJxP.html",{"respuesta":respuesta})

'''
ESTADIO
'''
def estadiosFormulario(request):
    if request.method =='POST':
        miFormulario=EstadiosFormulario(request.POST)
        if miFormulario.is_valid():
            info=miFormulario.cleaned_data
            nombre=info.get("nombre")
            capacidad=info.get("capacidad")
            estadio = Estadios(nombre=nombre, capacidad=capacidad)
            estadio.save()
            return render(request,"AppMundial/estadiosFormulario.html",{"mensaje": "Estadio creado, puede crear otro","formulario":miFormulario, "estadio":estadio.nombre})
        else:
            return render(request,"AppMundial/estadiosFormulario.html",{"mensaje": "ERROR","formulario":miFormulario})

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
        if miFormulario.is_valid():
            info=miFormulario.cleaned_data
            instancia=info.get("instancia")
            pais1=info.get("pais1")
            pais2=info.get("pais2")
            resultado=info.get("resultado")
            partido = Partidos(instancia=instancia, pais1=pais1, pais2=pais2, resultado=resultado)
            partido.save()
            return render(request,"AppMundial/partidosFormulario.html",{"mensaje": "Pais creado, puede crear otro","formulario":miFormulario, "equipo1": partido.pais1, "equipo2": partido.pais2})
        else:
            return render(request,"AppMundial/partidosFormulario.html",{"mensaje": "ERROR","formulario":miFormulario})

    else:
        miFormulario=PartidosFormulario()
        return render(request,"AppMundial/partidosFormulario.html",{"formulario":miFormulario})
    return render(request,"AppMundial/partidosFormulario.html")
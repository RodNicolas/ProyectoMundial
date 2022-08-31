from django.urls import path
from AppMundial import views
from .views import *

urlpatterns= [

    path('',views.inicio, name='inicio'),
    path('paises/',views.paises, name= 'paises'),
    path('jugadores/',views.jugadores, name='jugadores'),
    path('estadios/', views.estadios, name='estadios'),
    path('partidos/', views.partidos, name = 'partidos'),
    path('paisesFormulario/', views.paisesFormulario, name='paisesFormulario'),
    path('jugadoresFormulario/', views.jugadoresFormulario, name='jugadoresFormulario'),
    path('estadiosFormulario/', views.estadiosFormulario, name='estadiosFormulario'),
    path('partidosFormulario/', views.partidosFormulario, name='partidosFormulario'),
    path('busquedaJxP/', views.busquedaJxP, name='busquedaJxP'),
    path('buscar/', views.buscar),
    path('busquedaPxC/', views.busquedaPxC, name='busquedaPxC'),
    path('buscar2/', views.buscar2),
       
]

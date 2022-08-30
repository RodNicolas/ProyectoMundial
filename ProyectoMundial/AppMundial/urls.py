from django.urls import path
from AppMundial import views

urlpatterns= [

    path('',views.inicio, name='inicio'),
    path('paises',views.paises, name= 'paises'),
    path('jugadores',views.jugadores, name='jugadores'),
    path('estadios', views.estadios, name='estadios'),
    path('partidos', views.partidos, name = 'partidos'),

]

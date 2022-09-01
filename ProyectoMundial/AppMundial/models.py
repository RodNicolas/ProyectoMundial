from django.db import models

# Create your models here.
class Paises(models.Model):
    nombre=models.CharField(max_length=50)
    continente=models.CharField(max_length=50)
    grupo=models.CharField(max_length=1)

class Jugadores (models.Model):
    nombre=models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)
    edad=models.IntegerField()
    pais=models.CharField(max_length=50)
    equipo=models.CharField(max_length=50)

class Estadios (models.Model):
    nombre=models.CharField(max_length=50)
    capacidad=models.IntegerField()

class Partidos (models.Model):
    instancia=models.CharField(max_length=50)
    pais1=models.CharField(max_length=50)
    pais2=models.CharField(max_length=50)
    resultado=models.CharField(max_length=50, null=True)


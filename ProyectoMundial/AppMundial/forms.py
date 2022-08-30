from django import forms

class PaisesFormulario(forms.Form):
    nombre = forms.CharField(max_length=50)
    continente=forms.CharField(max_length=50)
    grupo=forms.CharField(max_length=1)


class JugadoresFormulario(forms.Form):
    nombre=forms.CharField(max_length=50)
    apellido=forms.CharField(max_length=50)
    edad=forms.IntegerField()
    pais=forms.CharField(max_length=50)
    equipo=forms.CharField(max_length=50)


class EstadiosFormulario(forms.Form):
    nombre=forms.CharField(max_length=50)
    capacidad=forms.IntegerField()


class PartidosFormulario(forms.Form):
    instancia=forms.CharField(max_length=50)
    pais1=forms.CharField(max_length=50)
    pais2=forms.CharField(max_length=50)
    resutlado=forms.CharField(max_length=10)


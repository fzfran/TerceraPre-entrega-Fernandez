from django import forms
from .models import Celulares  

class AddCel(forms.Form):
    marca = forms.CharField(max_length=20)
    modelo = forms.CharField(max_length=20)
    descripcion = forms.CharField(max_length=200)
    fecha_de_creacion = forms.IntegerField()
    
class AddNote(forms.Form):
    marca = forms.CharField(max_length=20)
    modelo = forms.CharField(max_length=20)
    fecha_de_creacion = forms.IntegerField()
    
class AddTele(forms.Form):
    marca = forms.CharField(max_length=20)
    modelo = forms.CharField(max_length=20)
    fecha_de_creacion = forms.IntegerField()

from django.shortcuts import render
from app1.models import Celulares, Notebooks,Televisores

# Create your views here.
def app1(request):
    return render(request, 'paginabase.html', {})

def celular(request):
    celulares = Celulares(marca='Apple',modelo='iPhone 11',fecha_de_creacion=2019)
    celulares.save()
    return render(request, 'celulares.html', {'celular':celulares})

def notebook(request):
    notebooks = Notebooks(marca='Asus', modelo='X533',fecha_de_creacion=2020)
    notebooks.save()
    return render(request,'notebooks.html', {'notebook':notebooks})

def televisor(request):
    televisores = Televisores(marca='Samsung', modelo='50 Pulgadas',fecha_de_creacion=2022)
    televisores.save()
    return render(request,'televisores.html', {'televisor':televisores})

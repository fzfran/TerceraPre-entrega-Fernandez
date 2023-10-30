from django.shortcuts import render, redirect
from app1.models import Celulares, Notebooks, Televisores
from app1.forms import AddCel, AddNote, AddTele

# Create your views here.
def app1(request):
    return render(request, 'paginabase.html', {})

def celular(request):
    marca_a_buscar = request.GET.get('marca')
    if marca_a_buscar:
        lista_de_celus = Celulares.objects.filter(marca__icontains=marca_a_buscar)
    else:    
        lista_de_celus = Celulares.objects.all()
    
    return render(request, 'celulares.html', {'lista_de_celus': lista_de_celus})


def add_celular(request):
    if request.method == 'POST':
          formulario = AddCel(request.POST)
          if formulario.is_valid():
              info_correcta = formulario.cleaned_data
              
              marca = info_correcta.get('marca')
              modelo = info_correcta.get('modelo')
              descripcion = info_correcta.get('descripcion')
              fecha_de_creacion = info_correcta.get('fecha_de_creacion')
              
              celulares = Celulares(marca=marca.lower(),modelo=modelo,descripcion=descripcion,fecha_de_creacion=fecha_de_creacion)
              celulares.save()
              return redirect('add_celular')
          
    formulario = AddCel() 
    return render(request, 'add_celu.html', {'formulario': formulario})
    



def notebook(request):
    marca_a_buscar = request.GET.get('marca')
    if marca_a_buscar:
        lista_de_note = Notebooks.objects.filter(marca__icontains=marca_a_buscar)
    else:    
        lista_de_note = Notebooks.objects.all()
    
    return render(request, 'notebooks.html', {'lista_de_note': lista_de_note})

def add_notebook(request):
    if request.method == 'POST':
          formulario = AddNote(request.POST)
          if formulario.is_valid():
              info_correcta = formulario.cleaned_data
              
              marca = info_correcta.get('marca')
              modelo = info_correcta.get('modelo')
              fecha_de_creacion = info_correcta.get('fecha_de_creacion')
              
              notebook = Notebooks(marca=marca.lower(),modelo=modelo,fecha_de_creacion=fecha_de_creacion)
              notebook.save()
              return redirect('add_notebook')
          
    formulario = AddNote() 
    return render(request, 'add_note.html', {'formulario': formulario})



def televisor(request):
    marca_a_buscar = request.GET.get('marca')
    if marca_a_buscar:
        lista_de_tele = Televisores.objects.filter(marca__icontains=marca_a_buscar)
    else:    
        lista_de_tele = Televisores.objects.all()
    
    return render(request, 'televisores.html', {'lista_de_tele': lista_de_tele})


def add_televisor(request):
    if request.method == 'POST':
          formulario = AddTele(request.POST)
          if formulario.is_valid():
              info_correcta = formulario.cleaned_data
              
              marca = info_correcta.get('marca')
              modelo = info_correcta.get('modelo')
              fecha_de_creacion = info_correcta.get('fecha_de_creacion')
              
              televisor = Televisores(marca=marca.lower(),modelo=modelo,fecha_de_creacion=fecha_de_creacion)
              televisor.save()
              return redirect('add_televisor')
          
    formulario = AddTele() 
    return render(request, 'add_tele.html', {'formulario': formulario})
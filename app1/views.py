from django.shortcuts import render, redirect
from app1.models import Celulares, Notebooks, Televisores
from app1.forms import AddCel, AddNote, AddTele, BaseForm
from django.contrib.auth.decorators import login_required

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

@login_required
def add_celular(request):
    if request.method == 'POST':
          formulario = AddCel(request.POST)
          if formulario.is_valid():
              info_correcta = formulario.cleaned_data
              
              marca = info_correcta.get('marca')
              modelo = info_correcta.get('modelo')
              descripcion = info_correcta.get('descripcion')
              fecha_de_creacion = info_correcta.get('fecha_de_creacion')
              
              celulares = Celulares(marca=marca,modelo=modelo,descripcion=descripcion,fecha_de_creacion=fecha_de_creacion)
              celulares.save()
              return redirect('Celulares')
          
    formulario = AddCel() 
    return render(request, 'add_celu.html', {'formulario': formulario})
@login_required
def eliminar(request, celular_id):
    celular_eliminar = Celulares.objects.get(id=celular_id)
    celular_eliminar.delete()
    return redirect('Celulares')

@login_required
def actualizar(request, celular_id):
    actualizar_celu = Celulares.objects.get(id=celular_id)
    if request.method == 'POST':
        formulario = BaseForm(request.POST)
        if formulario.is_valid():
            info_nueva = formulario.cleaned_data
            
            actualizar_celu.marca = info_nueva.get('marca')
            actualizar_celu.modelo = info_nueva.get('modelo')
            actualizar_celu.descripcion = info_nueva.get('descripcion')
            actualizar_celu.fecha_de_creacion = info_nueva.get('fecha_de_creacion')
            
            actualizar_celu.save()
            return redirect('Celulares')
        else:
            return render(request, 'actualizar_celu.html', {'formulario' :formulario})
    
    
    
    formulario = BaseForm(initial={'marca': actualizar_celu.marca, 'modelo': actualizar_celu.modelo, 'descripcion': actualizar_celu.descripcion, 'fecha_de_creacion': actualizar_celu.fecha_de_creacion})
    return render(request,'actualizar_celu.html', {'formulario': formulario})



def detalle_celu(request, celular_id):
    celular = Celulares.objects.get(id=celular_id)
    
    return render(request, 'detalle_celu.html', {'celular': celular})
    
    



def notebook(request):
    marca_a_buscar = request.GET.get('marca')
    if marca_a_buscar:
        lista_de_note = Notebooks.objects.filter(marca__icontains=marca_a_buscar)
    else:    
        lista_de_note = Notebooks.objects.all()
    
    return render(request, 'notebooks.html', {'lista_de_note': lista_de_note})

@login_required
def add_notebook(request):
    if request.method == 'POST':
          formulario = AddNote(request.POST)
          if formulario.is_valid():
              info_correcta = formulario.cleaned_data
              
              marca = info_correcta.get('marca')
              modelo = info_correcta.get('modelo')
              fecha_de_creacion = info_correcta.get('fecha_de_creacion')
              
              notebook = Notebooks(marca=marca,modelo=modelo,fecha_de_creacion=fecha_de_creacion)
              notebook.save()
              return redirect('Notebooks')
          
    formulario = AddNote() 
    return render(request, 'add_note.html', {'formulario': formulario})



def televisor(request):
    marca_a_buscar = request.GET.get('marca')
    if marca_a_buscar:
        lista_de_tele = Televisores.objects.filter(marca__icontains=marca_a_buscar)
    else:    
        lista_de_tele = Televisores.objects.all()
    
    return render(request, 'televisores.html', {'lista_de_tele': lista_de_tele})

@login_required
def add_televisor(request):
    if request.method == 'POST':
          formulario = AddTele(request.POST)
          if formulario.is_valid():
              info_correcta = formulario.cleaned_data
              
              marca = info_correcta.get('marca')
              modelo = info_correcta.get('modelo')
              fecha_de_creacion = info_correcta.get('fecha_de_creacion')
              
              televisor = Televisores(marca=marca,modelo=modelo,fecha_de_creacion=fecha_de_creacion)
              televisor.save()
              return redirect('Televisores')
          
    formulario = AddTele() 
    return render(request, 'add_tele.html', {'formulario': formulario})


def aboutme(request):
    return render(request, 'aboutme.html', {})

def mi_vista(request):
    imagen_url = '/static/assets/img/celuz.jpg'
    return render(request, 'celulares.html', {'imagen_url': imagen_url})
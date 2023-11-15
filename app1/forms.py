from django import forms

class BaseForm(forms.Form):
    marca = forms.CharField(max_length=20)
    modelo = forms.CharField(max_length=20)
    descripcion = forms.CharField(max_length=200)
    fecha_de_creacion = forms.IntegerField()


class AddCel(BaseForm):
    ...
class ActualizarCel(BaseForm):
    ...   
class AddNote(BaseForm):
    ...    
class AddTele(BaseForm):
    ...

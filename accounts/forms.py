from django import forms 
from ckeditor.fields import RichTextFormField
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User

class myForm(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir Contraseña', widget=forms.PasswordInput)
    
    class Meta:
         model = User
         fields = ['username', 'email' , 'password1', 'password2']
         help_texts = {key: '' for key in fields}
         
         
class EditForm(UserChangeForm):
    password = None
    email = forms.EmailField(label='Cambiar Email')
    first_name = forms.CharField(label='Cambiar Nombre', required=False)
    last_name = forms.CharField(label='Cambiar Apellido', required=False)
    biografia = RichTextFormField()
    avatar = forms.ImageField(required=False)
    
    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name', 'biografia', 'avatar']
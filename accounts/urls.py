from django.urls import path
from .views import login, registro, editar_perfil, perfil ,CambiarPassword
from django.contrib.auth.views import LogoutView
urlpatterns = [
    path('login/', login, name='login'),
    path('logout/', LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('registro/', registro, name='registrarse'),
    path('perfil/', perfil , name='perfil'),
    path('perfil/editar/', editar_perfil , name='editar_perfil'),
    path('perfil/editar/password/', CambiarPassword.as_view(template_name='cambiar_password.html'),name='cambiar_password')
]

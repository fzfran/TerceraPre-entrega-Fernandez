from django.urls import path
from app1.views import app1, celular, notebook, televisor, add_celular, add_notebook, add_televisor

urlpatterns = [
    path('', app1, name='Inicio'),
    path('celular/', celular, name='Celulares'),
    path('add_celular/', add_celular, name='add_celular'),
    path('notebooks/', notebook, name='Notebooks'),
    path('add_notebook/', add_notebook, name='add_notebook'),
    path('televisores/', televisor, name='Televisores'),
    path('add_televisor/', add_televisor, name='add_televisor'),
]

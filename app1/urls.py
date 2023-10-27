from django.urls import path
from app1.views import app1, celular, notebook, televisor

urlpatterns = [
    path('', app1, name='Inicio'),
    path('celular/', celular, name='Celulares'),
    path('notebooks/', notebook, name='Notebooks'),
    path('televisores/', televisor, name='Televisores'),
]

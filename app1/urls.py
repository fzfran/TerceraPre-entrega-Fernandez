from django.urls import path
from app1.views import app1, celular, notebook, televisor, add_celular, add_notebook, add_televisor, eliminar, actualizar, detalle_celu, aboutme

urlpatterns = [
    path('', app1, name='Inicio'),
    path('aboutme/', aboutme , name='aboutme' ),
    path('celular/', celular, name='Celulares'),
    path('add_celular/', add_celular, name='add_celular'),
    path('celular/<int:celular_id>/actualizar/', actualizar, name='actualizar_celu'),
    path('celular/<int:celular_id>/eliminar/', eliminar, name='eliminar_celu'),
    path('celular/<int:celular_id>/', detalle_celu, name='detalle_celu'),
    path('notebooks/', notebook, name='Notebooks'),
    path('add_notebook/', add_notebook, name='add_notebook'),
    path('televisores/', televisor, name='Televisores'),
    path('add_televisor/', add_televisor, name='add_televisor'),
]

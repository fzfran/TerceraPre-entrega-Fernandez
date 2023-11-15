from django.urls import path
from .views import ListadoPerifericos, PerifericoModelCreateView, ActualizarPeriferico, DetallePeriferico, BorrarPeriferico

urlpatterns = [
    path('perifericos/', ListadoPerifericos.as_view() , name='perifericos' ),
    path('perifericos/crear/', PerifericoModelCreateView.as_view() , name='crear_perifericos' ),
    path('perifericos/<int:pk>/', DetallePeriferico.as_view() , name='detalle_perifericos' ),
    path('perifericos/<int:pk>/eliminar/', BorrarPeriferico.as_view() , name='eliminar_perifericos' ),
    path('perifericos/<int:pk>/actualizar/', ActualizarPeriferico.as_view() , name='actualizar_perifericos' ),
]

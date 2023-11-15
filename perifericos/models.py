from django.db import models

# Create your models here.

class Periferico(models.Model):
    marca = models.CharField(max_length=30)
    modelo = models.CharField(max_length=30)
    fecha_de_creacion = models.DateField()
    
    def __str__(self):
        return f'{self.marca} - {self.modelo} - {self.fecha_de_creacion}'
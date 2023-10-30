from django.contrib import admin
from app1.models import Celulares, Notebooks, Televisores

# Register your models here.

admin.site.register({Celulares, Notebooks, Televisores})

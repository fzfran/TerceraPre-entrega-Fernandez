from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User

# Create your models here.

class DatosExtra(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    biografia = RichTextField()
    avatar = models.ImageField(upload_to='avatares', null=True, blank=True)
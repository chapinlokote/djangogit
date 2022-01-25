from django.db import models
from django.forms import CharField
import datetime
from django.utils import timezone
import pytz

# Create your models here.
class Participantes(models.Model):
    codigo = models.CharField(primary_key=True, max_length=4)
    nombre = models.CharField(max_length=50)
    correo = models.CharField(max_length=50)
    celular = models.CharField(max_length=6)
    #fecha_actualizado = models.DateTimeField(auto_now_add=False, auto_now=True, blank=True)

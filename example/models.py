from django.db import models
from django.contrib.auth.models import User

# Create your views here.

class Actividad(models.Model):
    name = models.CharField(max_length=30, null=False)
    date = models.DateField(null=False)
    hour = models.CharField(max_length=30)
    class Meta:
        db_table = "actividades"

class Cosa(models.Model):
    actividad_id = models.ForeignKey(Actividad, on_delete=models.SET(-1))#, related_name='inventario'
    name = models.CharField(max_length=30, null=False)

    class Meta:
        db_table = "cosas"



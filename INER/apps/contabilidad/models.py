from __future__ import unicode_literals
from __future__ import absolute_import
from django.db import models



# Create your models here.
class Contabilidad(models.Model):
    clave_cucop = models.CharField(max_length=200)
    partida = models.IntegerField()
    descripcion = models.CharField(max_length=400)
    unidad_medida = models.CharField(max_length=400)
    def __str__(self):
		return '{}'.format(self.clave_cucop)

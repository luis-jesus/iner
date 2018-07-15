from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Pago(models.Model):
    partida = models.IntegerField()
    art_laassp = models.CharField(max_length = 400)
    no_contrato = models.CharField(max_length = 400)
    prov_adju = models.CharField(max_length = 400)
    fecha_inicio = models.DateField(auto_now=False, auto_now_add=False)
    fecha_termino = models.DateField(auto_now=False, auto_now_add=False)
    obje_contrato = models.CharField(max_length = 400)
    fir_contrato = models.DateField(auto_now=False, auto_now_add=False)
    monto_contraiva = models.DecimalField(max_digits=200, decimal_places=2)
    convenios = models.CharField(max_length = 400)
    deductivas = models.CharField(max_length = 400)
    dis_contrato = models.CharField(max_length = 400)
    total_contrato = models.DecimalField(max_digits=200, decimal_places=2)
    area_respon = models.CharField(max_length = 400)
    for_pago = models.CharField(max_length = 400)

    def __str__(self):
        return self.no_contrato

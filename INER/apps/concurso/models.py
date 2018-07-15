from __future__ import unicode_literals
from __future__ import absolute_import
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
from multiselectfield import MultiSelectField
from django.db import models

operacion_choises = (
    ('Bienes', 'Bienes'),
    ('Servicios', 'Servicios'),
    ('Obras', 'Obras'),
)
procedimiento_choises = (
    ('Licitacion Nacional', 'Licitacion Nacional'),
    ('Licitacion Internacional', 'Licitacion Internacional'),
    ('Adjudicacion Directa', 'Adjudicacion Directa'),
    ('Invitacion a 3 Provedores', 'Invitacion a 3 Provedores'),
)
precios_choises = (
    ('Fijos', 'Fijos'),
    ('Variables', 'Variables'),
    ('Unitarios', 'Unitarios'),
    ('Alazados', 'Alazados'),
    ('Mixtos', 'Mixtos'),
)

contratacion_choises = (
    ('Abierto', 'Abierto'),
    ('Cerrado', 'Cerrado'),
)

plurianual_choises = (
    ('Si', 'Si'),
    ('No', 'No'),
)

convenio_choises = (
    ('Si', 'Si'),
    ('No', 'No'),
)
# Create your models here.
class Contrato(models.Model):
    no_contrato = models.CharField(max_length=200)
    tipo_procedimiento = models.CharField(max_length=200, choices=procedimiento_choises)
    descripcion_servicio = models.CharField(max_length=400)
    provedor = models.CharField(max_length=400)
    area_solicitante = models.CharField(max_length=400)
    monto_contrato_siniva = models.DecimalField(max_digits=200, decimal_places=2)
    iva = models.DecimalField(max_digits=200, decimal_places=2)
    monto_total = models.DecimalField(max_digits=200, decimal_places=2)
    fecha_inicio = models.DateField(auto_now=False,auto_now_add=False)
    fecha_termino = models.DateField(auto_now=False,auto_now_add=False)
    fecha_contratacion = models.DateField(auto_now=False,auto_now_add=False)
    observaciones = models.CharField(max_length=400)
    status = models.CharField(max_length=200)
    rfc = models.CharField(max_length=200)
    representante_legal = models.CharField(max_length=200)
    tipo_operacion = models.CharField(max_length=400, choices=operacion_choises)
    esquema_precios = models.CharField(max_length=200, choices=precios_choises)
    tipo_contratacion = models.CharField(max_length=200, choices=contratacion_choises)
    plurianual = models.CharField(max_length=200, choices=plurianual_choises)
    tipo_moneda = models.CharField(max_length=200)
    monto_vigente = models.DecimalField(max_digits=200, decimal_places=2)
    monto_total_minima = models.DecimalField(max_digits=200, decimal_places=2)
    monto_total_maximo = models.DecimalField(max_digits=200, decimal_places=2)
    convenio_modificatorio = models.CharField(max_length=200, choices=convenio_choises)
    no_convenio = models.CharField(max_length=200)
    fecha_modificacion_convenio = models.DateField(auto_now=False,auto_now_add=False)

    def __str__(self):
		return '{}'.format(self.no_contrato)

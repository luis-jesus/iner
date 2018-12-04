from __future__ import unicode_literals
from __future__ import absolute_import
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
from multiselectfield import MultiSelectField
from smart_selects.db_fields import ChainedForeignKey, GroupedForeignKey
from django.db import models
from apps.contabilidad.models import Contabilidad

lugar_choises = (
    ('Instituto Nacional de Enfermedades Respiratorias "Ismael Cosio Villegas"',
    'Instituto Nacional de Enfermedades Respiratorias "Ismael Cosio Villegas"'),
    )
cantidad_choises = (
    ('1', '1'),
    )
unididad_choises = (
    ('Servicio', 'Servicio'),
    )
entrega_choices = (
    ('Calz Tlalpan No. 4502 Secc. XVI Bel. Dom. CP. 14080', 'Calz Tlalpan No. 4502 Secc. XVI Bel. Dom. CP. 14080'),
    )

anticipo_choices = (
    ('SI','SI'),
    ('NO','NO'),
    )

almacen_choices = (
    ('N/A','N/A'),
    )

pais_choices = (
    ('Nacional (Mexico)','Nacional (Mexico)'),
    )

garantia1_choices = (
    ('N/A','N/A'),
    ('Anticipo','Anticipo'),
    ('Cumplimiento divisible','Cumplimiento divisible'),
    ('Cumplimiento indivisible','Cumplimiento indivisible'),
    ('Vicios ocultos','Vicios ocultos'),
    ('Defectos o Calidad/Poliza de responsbilidad civil/otra','Defectos o Calidad/Poliza de responsbilidad civil/otra'),
    )

garantia2_choices = (
    ('N/A','N/A'),
    ('Anticipo','Anticipo'),
    ('Cumplimiento divisible','Cumplimiento divisible'),
    ('Cumplimiento indivisible','Cumplimiento indivisible'),
    ('Vicios ocultos','Vicios ocultos'),
    ('Defectos o Calidad/Poliza de responsbilidad civil/otra','Defectos o Calidad/Poliza de responsbilidad civil/otra'),
    )
garantia3_choices = (
    ('N/A','N/A'),
    ('Anticipo','Anticipo'),
    ('Cumplimiento divisible','Cumplimiento divisible'),
    ('Cumplimiento indivisible','Cumplimiento indivisible'),
    ('Vicios ocultos','Vicios ocultos'),
    ('Defectos o Calidad/Poliza de responsbilidad civil/otra','Defectos o Calidad/Poliza de responsbilidad civil/otra'),
    )

plurianualidad_choices = (
    ('SI', 'SI'),
    ('NO', 'NO'),
    )
penas_choices = (
    ('SI', 'SI'),
    ('NO', 'NO'),
    )

fabricacion_choices = (
    ('N/A','N/A'),
    )

anexo_choices = (
    ('SI', 'SI'),
    ('NO', 'NO'),
    )


# Create your models here.
class Focon(models.Model):
    no_focon = models.CharField(max_length=200)
    no_oficio = models.CharField(max_length=200)
    area_requirente = models.CharField(max_length=400)
    descripcion = models.CharField(max_length=400)
    partida = models.IntegerField()
    descripcion_servicio = models.CharField(max_length=400)
    monto_civa = models.DecimalField(max_digits=200, decimal_places=2)
    fecha_solicitud = models.DateField(auto_now=False,auto_now_add=False)
    fecha_envio = models.DateField(auto_now=False,auto_now_add=False)
    entrega_requirente = models.DateField(auto_now=False, auto_now_add=False)
    status = models.CharField(max_length=200)
    autorizacion_babel = models.CharField(max_length=200)

    def __str__(self):
		return '{}'.format(self.descripcion)

class Catalogofocon(models.Model):
    partidacatalogo = models.IntegerField()
    obj_contra = models.CharField(max_length=400)

    def __unicode__ (self):
        return u'{f}'.format(f=self.obj_contra)

class Focon03(models.Model):
    dependencia = models.CharField(max_length=400, choices=lugar_choises)
    area_requirente = models.CharField(max_length=400)
    fecha_elaboracion = models.DateField(auto_now=False, auto_now_add=False)
    no_requisicion = models.CharField(max_length=400, null=True, blank=True)
    fecha_requerida = models.DateField(auto_now=False, auto_now_add=False)
    lugar_entrega = models.CharField(max_length=400, choices = entrega_choices)
    partida = models.IntegerField()
    clave_cucop = models.ForeignKey(Contabilidad)
    descripcion = models.CharField(max_length=400)
    descripcion_detallada = models.CharField(max_length=400)
    cantidad_solicitada = models.CharField(max_length=400, choices=cantidad_choises)
    unidad_medida = models.CharField(max_length=400, choices= unididad_choises)
    precio_unitario = models.DecimalField(max_digits=200, decimal_places=2)
    importe = models.DecimalField(max_digits=200, decimal_places=2)
    subtotal = models.DecimalField(max_digits=200, decimal_places=2)
    iva = models.DecimalField(max_digits=200, decimal_places=2)
    otros_gravamenes = models.DecimalField(max_digits=200, decimal_places=2, null=True, blank=True)
    total = models.DecimalField(max_digits=200, decimal_places=2)
    anexos = models.CharField(max_length=400, choices=anexo_choices)
    anticipo = models.CharField(max_length=400, choices=anticipo_choices)
    autorizacion_presupuesto = models.CharField(max_length=400)
    existencia_almacen = models.CharField(max_length=400, choices=almacen_choices)
    observaciones = models.CharField(max_length=400)
    registro_sanitario = models.CharField(max_length=400)
    normas = models.CharField(max_length=400)
    capacitacion = models.CharField(max_length=400)
    pais_origen = models.CharField(max_length=400, choices = pais_choices)
    metodo_prueba = models.CharField(max_length=400)
    tipo_garantia1 = models.CharField(max_length=400, choices = garantia1_choices)
    tipo_garantia2 = models.CharField(max_length=400, choices = garantia2_choices)
    tipo_garantia3 = models.CharField(max_length=400, choices = garantia3_choices)
    porcentaje1 = models.CharField(max_length=400)
    porcentaje2 = models.CharField(max_length=400)
    porcentaje3 = models.CharField(max_length=400)
    plurianualidad = models.CharField(max_length=400, choices = plurianualidad_choices)
    meses = models.CharField(max_length=400)
    penas_convencionales = models.CharField(max_length=400, choices = penas_choices)
    porcentaje_penas = models.CharField(max_length=400)
    tiempo_fabricacion = models.CharField(max_length=400, choices = fabricacion_choices)
    condiciones_entrega = models.CharField(max_length=400)
    solicita = models.CharField(max_length=400)
    autoriza = models.CharField(max_length=400)

    def __unicode__ (self):
        return u'{f}'.format(f=self.no_requisicion)

    # def __unicode__ (self):
    #     return u'{f}'.format(f=self.descripcion)

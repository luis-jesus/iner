from django import forms
from .models import Pago
from django.forms import ModelForm, TextInput, DateField, NumberInput, SelectDateWidget

class PagoForm(forms.ModelForm):
	class Meta:
		model = Pago
		fields = [
			'partida',
			'art_laassp',
			'no_contrato',
			'prov_adju',
			'fecha_inicio',
			'fecha_termino',
			'obje_contrato',
			'fir_contrato',
			'monto_contraiva',
			'convenios',
			'deductivas',
			'dis_contrato',
            'total_contrato',
            'area_respon',
            'for_pago',
		]

		labels = {
			'partida':'Partida',
			'art_laassp':'ART LAASSP',
			'no_contrato':'No de Contrato',
			'prov_adju':'Proveedor',
			'fecha_inicio':'Fecha de Inicio',
			'fecha_termino':'Fecha de Termino',
			'obje_contrato':'Objeto de Contrato',
			'fir_contrato':'Firma de Contrato',
			'monto_contraiva':'Monto de Contrato C/IVA',
			'convenios':'Convenios',
			'deductivas':'Deductivas',
			'dis_contrato':'Contrato',
            'total_contrato':'Total de Contrato',
            'area_respon':'Area Responsable',
            'for_pago':'Forma de Pago',
		}
		widgets = {
			'partida':forms.TextInput(attrs={'class':'form-control'}),
			'art_laassp':forms.TextInput(attrs={'class':'form-control'}),
			'no_contrato':forms.TextInput(attrs={'class':'form-control'}),
			'prov_adju':forms.TextInput(attrs={'class':'form-control'}),
			'fecha_inicio':forms.SelectDateWidget(attrs={'class':'form-control'}),
			'fecha_termino':forms.SelectDateWidget(attrs={'class':'form-control'}),
			'obje_contrato':forms.TextInput(attrs={'class':'form-control'}),
			'fir_contrato':forms.SelectDateWidget(attrs={'class':'form-control'}),
			'monto_contraiva':forms.TextInput(attrs={'class':'form-control'}),
			'convenios':forms.TextInput(attrs={'class':'form-control'}),
			'deductivas':forms.TextInput(attrs={'class':'form-control'}),
			'dis_contrato':forms.TextInput(attrs={'class':'form-control'}),
            'total_contrato':forms.TextInput(attrs={'class':'form-control'}),
            'area_respon':forms.TextInput(attrs={'class':'form-control'}),
            'for_pago':forms.TextInput(attrs={'class':'form-control'}),
		}

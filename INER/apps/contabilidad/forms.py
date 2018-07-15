from django import forms
from .models import Contabilidad


class ContabilidadForm(forms.ModelForm):
    class Meta:
        model = Contabilidad
        fields = '__all__'

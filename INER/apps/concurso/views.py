from __future__ import absolute_import
from django.conf import settings
from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import View
from django.views.generic import ListView, TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.edit import (
    CreateView,
    UpdateView,
    DeleteView
)
from apps.concurso.models import Contrato
from apps.concurso.forms import ConcursoForm
#PDF
from reportlab.pdfgen import canvas
from reportlab.platypus import SimpleDocTemplate, Paragraph, TableStyle
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.platypus import Table
from io import BytesIO
from reportlab.lib.colors import PCMYKColor
from reportlab.lib.pagesizes import letter, landscape

class ConcursoList(ListView):
    model = Contrato
    template_name = 'concurso/con_list.html'

class ConcursoCreation(CreateView):
    model = Contrato
    success_url = reverse_lazy('concurso:list')
    form_class = ConcursoForm
    template_name = 'concurso/con_form.html'

class ConcursoUpdate(UpdateView):
    model = Contrato
    success_url = reverse_lazy('concurso:list')
    form_class = ConcursoForm
    template_name = 'concurso/con_edit.html'

    def focon_view(request):
    	if request.method == 'POST':
    		form = ConcursoForm(request.POST)
    		if form.is_valid():
    			form.save()
    		return redirect('concurso:list')
    	else:
    		form = ConcursoForm()
    	return render(request, 'concurso/con_form.html',{'form':form})

    def focon_list(request):
    	focon = Contrato.objects.all().order_by('id')
    	contexto = {'concurso':concurso}
    	return render(request, 'concurso/con_list.html',contexto)

class ConcursoDelete(DeleteView):
    model = Contrato
    success_url = reverse_lazy('concurso:list')
    template_name = 'concurso/con_delete.html'

#PDF
class ReporteConcursoPDF(View):
    def cabecera(self,pdf):
        archivo_imagen = settings.MEDIA_ROOT+'/imagenes/INER.jpg'
        pdf.drawImage(archivo_imagen, 40, 750, 120, 90,preserveAspectRatio=True)
        pdf.setFont("Helvetica", 16)
        pdf.drawString(180, 790, u"Instituto Nacional de Enfermedades Respiratorias")
        pdf.setFont("Helvetica", 14)
        pdf.drawString(200, 770, u"REPORTE GENERAL")

    def get(self, request, *args, **kwargs):
        response = HttpResponse(content_type='application/pdf')
        pdf_name = "ReporteGeneral.pdf"
        # la linea 26 es por si deseas descargar el pdf a tu computadora
        # response['Content-Disposition'] = 'attachment; filename=%s' % pdf_name
        buffer = BytesIO()
        pdf = canvas.Canvas(buffer)
        pdf.setTitle("Reporte General")
        self.cabecera(pdf)
        y = 600
        self.tabla(pdf, y)
        pdf.showPage()
        pdf.save()
        pdf = buffer.getvalue()
        buffer.close()
        response.write(pdf)
        return response

    def tabla(self,pdf,y):
        encabezados = ('No de Contrato', 'Tipo de Procedimiento', 'Proveedor', 'Area Solicitante')
        detalles = [(cu.no_contrato, cu.tipo_procedimiento, cu.provedor, cu.area_solicitante) for cu in Contrato.objects.all()]
        detalle_orden = Table([encabezados] + detalles)
        detalle_orden.setStyle(TableStyle(
        [
                ('ALIGN',(0,0),(3,0),'CENTER'),
                ('GRID', (0, 0), (-1, -1), 1, colors.black),
                ('FONTSIZE', (0, 0), (-1, -1), 10),
                ]
        ))

        detalle_orden.wrapOn(pdf, 800, 600)
        detalle_orden.drawOn(pdf, 60,y)

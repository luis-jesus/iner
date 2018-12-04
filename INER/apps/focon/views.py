from __future__ import absolute_import
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponse, HttpResponseRedirect
from django.template.loader import get_template
from django.views.generic import ListView, TemplateView, View
from django.views.generic.detail import DetailView
from django.views.generic.edit import (
    CreateView,
    UpdateView,
    DeleteView
)
from apps.focon.models import Focon, Catalogofocon, Focon03
from apps.contabilidad.models import Contabilidad
from apps.focon.forms import Focon03Form, FoconForm
from apps.contabilidad.forms import ContabilidadForm
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
#HTMLtoPDF
from wkhtmltopdf.views import PDFTemplateView
from wkhtmltopdf.views import PDFTemplateResponse
from reportlab.lib.pagesizes import letter, landscape
# from apps.focon.utils import render_to_pdf
from django.http import JsonResponse
from django.core.serializers.json import DjangoJSONEncoder
import json

class FoconList(ListView):
    model = Focon
    template_name = 'focon/foc_list.html'

class FoconCreation(CreateView):
    model = Focon
    success_url = reverse_lazy('focon:list')
    form_class = FoconForm
    template_name = 'focon/foc_form.html'

class FoconUpdate(UpdateView):
    model = Focon
    success_url = reverse_lazy('focon:list')
    form_class = FoconForm
    template_name = 'focon/foc_edit.html'

    def focon_view(request):
    	if request.method == 'POST':
    		form = FoconForm(request.POST)
    		if form.is_valid():
    			form.save()
    		return redirect('focon:list')
    	else:
    		form = FoconForm()
    	return render(request, 'focon/foc_form.html',{'form':form})

    def focon_list(request):
    	focon = Focon.objects.all().order_by('id')
    	contexto = {'focon':focon}
    	return render(request, 'focon/foc_list.html',contexto)

class FoconDelete(DeleteView):
    model = Focon
    success_url = reverse_lazy('focon:list')
    template_name = 'focon/foc_delete.html'

#PDF
class ReporteFoconPDF(View):
    def cabecera(self,pdf):
        archivo_imagen = settings.MEDIA_ROOT+'/imagenes/INER.jpg'
        pdf.drawImage(archivo_imagen, 40, 750, 120, 90,preserveAspectRatio=True)
        pdf.setFont("Helvetica", 16)
        pdf.drawString(180, 790, u"Instituto Nacional de Enfermedades Respiratorias")
        pdf.setFont("Helvetica", 14)
        pdf.drawString(200, 770, u"REPORTE GENERAL")

    def get(self, request, *args, **kwargs):
        response = HttpResponse(content_type='application/pdf')
        pdf_name = "ReporteGeneral.pdf"  # nombre del archivo PDF
        # la linea 87 es por si deseas descargar el pdf a tu computadora
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
        encabezados = ('No de Focon', 'No de Oficio', 'Area Requirente', 'Partida',  'Fecha de Solicitud', 'Fecha de Envio')
        detalles = [(fo.no_focon, fo.no_oficio, fo.area_requirente,  fo.partida,  fo.fecha_solicitud, fo.fecha_envio) for fo in Focon.objects.all()]
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



#Catalogo Focon

class CatalogoList(ListView):
    model = Catalogofocon
    template_name = 'focon/catalogo/cat_list.html'

class CatalogoCreation(CreateView):
    model = Catalogofocon
    success_url = reverse_lazy('focon:clist')
    fields = ['partidacatalogo', 'obj_contra']
    template_name = 'focon/catalogo/cat_form.html'

class CatalogoUpdate(UpdateView):
    model = Catalogofocon
    success_url = reverse_lazy('focon:clist')
    fields = ['partidacatalogo', 'obj_contra']
    template_name = 'focon/catalogo/cat_edit.html'

class CatalogoDelete(DeleteView):
    model = Catalogofocon
    success_url = reverse_lazy('focon:clist')
    template_name = 'focon/catalogo/cat_delete.html'


#Focon03
@login_required
def Focon03List(request):
    if request.user.is_superuser:
        query = Focon03.objects.order_by('id')
    else:
        query = Focon03.objects.filter(area_requirente=request.user.username)
    context = {
    'lista':query,
    }
    print(query)
    return render(request, 'focon/focon03/03_list.html', context)


@login_required
def Focon03Creation(request):
    form = Focon03Form(request.POST or None)
    foconlista = Contabilidad.objects.order_by('clave_cucop')
    foconlist1 = list(Contabilidad.objects.order_by('clave_cucop').values_list())
    fo_list2 = []
    for abc in foconlist1:
        fo_list2.append({
        'pk':abc[0],
        'clave_cucop':abc[1],
        'partida':abc[2],
        'descripcion':abc[3],
        'unidad_medida':abc[4]
        })
    foconlist3 = json.dumps(fo_list2, cls=DjangoJSONEncoder)
    context = {
    'form':form,
    'foconlista':foconlista,
    'foconlist1':foconlist3,
    }
    if request.method == 'POST':
        form = Focon03Form(request.POST)
        if form.is_valid():
            form.save()
        return redirect('focon:f03list')
            # return HttpResponseRedirect(reverse('focon/focon03/03_list.html'))
    else:
        form = Focon03Form()
    return render(request, 'focon/focon03/03_form.html', context)

class Focon03Detail(DetailView):
    model = Focon03
    template_name = 'focon/focon03/03_detail.html'

class Focon03Update(UpdateView):
    model = Focon03
    success_url = reverse_lazy('focon:f03list')
    form_class = Focon03Form
    template_name = 'focon/focon03/03_edit.html'

class Focon03Delete(DeleteView):
    model = Focon03
    success_url = reverse_lazy('focon:f03list')
    template_name = 'focon/focon03/03_delete.html'

class MyPDFView(DetailView):
    model = Focon03
    template='focon/focon03/03_detail.html'
    foconlista = Contabilidad.objects.order_by('pk')
    context= {
    'foconlista':foconlista
    }
    def get(self, request, *args, **kwargs):
        self.context['focon'] = self.get_object()

        response=PDFTemplateResponse(request=request,
                                     template=self.template,
                                     filename ="focon03.pdf",
                                     context=self.context,
                                     show_content_in_browser=True,
                                     cmd_options={'margin-top': 50,}
                                     )
        return response



# class MyPDF(PDFTemplateView):
#     filename = 'focon03.pdf'
#     template_name = 'focon/focon03/03_detail.html'
#     cmd_options = {
#         'margin-top': 3,
#     }


# class GeneratePDF(View):
#      def get(self, request, *args, **kwargs):
#          focon = Focon03.objects.all().order_by('id')
#          template = get_template('focon/focon03/03_detail.html')
#          context = {
#              'focon':focon
#          }
#          html = template.render(context)
#          pdf = render_to_pdf('focon/focon03/03_detail.html', context)
#          if pdf:
#              response = HttpResponse(pdf, content_type='application/pdf')
#              filename = "Invoice_%s.pdf" %("12341231")
#              content = "inline; filename='%s'" %(filename)
#              download = request.GET.get("download")
#              if download:
#                  content = "attachment; filename='%s'" %(filename)
#              response['Content-Disposition'] = content
#              return response
#          return HttpResponse("Not found")

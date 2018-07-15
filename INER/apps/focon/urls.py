from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from wkhtmltopdf.views import PDFTemplateView
from . import views
app_name = 'Focon'
from .views import (
    FoconList,
    FoconCreation,
    FoconUpdate,
    FoconDelete,
    ReporteFoconPDF,
    CatalogoList,
    CatalogoCreation,
    CatalogoUpdate,
    CatalogoDelete,
    Focon03List,
    Focon03Creation,
    Focon03Update,
    Focon03Delete,
    Focon03Detail,
    # MyPDFView,

)
urlpatterns = [
    #Focon03
    url(r'^focon03$', Focon03List, name='f03list'),
    url(r'^nuevo/focon03$', Focon03Creation, name='f03new'),
    url(r'^(?P<pk>\d+)$', login_required(Focon03Detail.as_view()), name='f03detail'),
    url(r'^editar/f03/(?P<pk>\d+)$', login_required(Focon03Update.as_view()), name='f03edit'),
    url(r'^borrar/f03/(?P<pk>\d+)$', login_required(Focon03Delete.as_view()), name='f03delete'),
    # url(r'^pdf/f03/$', views.MyPDFView.as_view(), name='pagina_detalle'),
    # url(r'^pdf/f03/$', PDFTemplateView.as_view(template_name='focon/focon03/03_detail.html',filename='focon03.pdf'), name='pdf'),
    # url(r'^/(?P<pk>\d+)/$', MyPDFView.as_view(), name='book-detail'),

    #Focon
    url(r'^$', login_required(FoconList.as_view()), name='list'),
    url(r'^nuevo$', login_required(FoconCreation.as_view()), name='new'),
    url(r'^editar/(?P<pk>\d+)$', login_required(FoconUpdate.as_view()), name='edit'),
    url(r'^borrar/(?P<pk>\d+)$', login_required(FoconDelete.as_view()), name='delete'),
    url(r'^pdf/$', login_required(ReporteFoconPDF.as_view()), name="reporte_personas_pdf"),

    #Catalogo
    url(r'^catalogo$', login_required(CatalogoList.as_view()), name='clist'),
    url(r'^nuevo/catalogo$', login_required(CatalogoCreation.as_view()), name='cnew'),
    url(r'^editar/catalogo(?P<pk>\d+)$', login_required(CatalogoUpdate.as_view()), name='cedit'),
    url(r'^borrar/catalogo(?P<pk>\d+)$', login_required(CatalogoDelete.as_view()), name='cdelete'),
]

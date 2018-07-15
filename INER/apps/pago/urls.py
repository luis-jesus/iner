from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from django.contrib.auth import views as auth_views
from . import views
app_name = 'Focon'
from .views import(
    PagoList,
    PagoCreation,
    PagoDetail,
    PagoUpdate,
    PagoDelete,
    ReportePagoPDF
)

urlpatterns = [
    url(r'^$', login_required(PagoList.as_view()), name='list'),
    url(r'^nuevo$', login_required(PagoCreation.as_view()), name='new'),
    url(r'^(?P<pk>\d+)$', login_required(PagoDetail.as_view()), name='detail'),
    url(r'^editar/(?P<pk>\d+)$', login_required(PagoUpdate.as_view()), name='edit'),
    url(r'^borrar/(?P<pk>\d+)$', login_required(PagoDelete.as_view()), name='delete'),
    url(r'^pdf/$', login_required(ReportePagoPDF.as_view()), name="reporte_personas_pdf"),

]

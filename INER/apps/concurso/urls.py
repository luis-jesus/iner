from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from . import views
app_name = 'concurso'
from .views import (
    ConcursoList,
    ConcursoCreation,
    ConcursoUpdate,
    ConcursoDelete,
    ReporteConcursoPDF

)


urlpatterns = [
    url(r'^$', login_required(ConcursoList.as_view()), name='list'),
    url(r'^nuevo$', login_required(ConcursoCreation.as_view()), name='new'),
    url(r'^editar/(?P<pk>\d+)$', login_required(ConcursoUpdate.as_view()), name='edit'),
    url(r'^borrar/(?P<pk>\d+)$', login_required(ConcursoDelete.as_view()), name='delete'),
    url(r'^pdf/$',login_required(ReporteConcursoPDF.as_view()), name="reporte_personas_pdf"),


]

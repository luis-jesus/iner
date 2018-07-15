from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from . import views
app_name = 'Contabilidad'
from .views import (
    ContabilidadList,
    ContabilidadDetail,
    ContabilidadCreation,
    ContabilidadUpdate,
    ContabilidadDelete,
    ReporteCucopExcel
)
urlpatterns = [
    url(r'^$', login_required(ContabilidadList.as_view()), name='list'),
    url(r'^(?P<pk>\d+)$', login_required(ContabilidadDetail.as_view()), name='detail'),
    url(r'^nuevo$', login_required(ContabilidadCreation.as_view()), name='new'),
    url(r'^editar/(?P<pk>\d+)$', login_required(ContabilidadUpdate.as_view()), name='edit'),
    url(r'^borrar/(?P<pk>\d+)$', login_required(ContabilidadDelete.as_view()), name='delete'),
    url(r'^excel/', login_required(ReporteCucopExcel.as_view()), name="reporteexcel"),
]

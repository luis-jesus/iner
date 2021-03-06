"""INER URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.conf import settings
from django.contrib import admin
from django.conf.urls.static import static
from .views import home_page
# from .views import GeneratePDF
# from apps.focon import views as anidadosviews
# admin.autodiscover()



urlpatterns = [
    url(r'^D.M.C.C-INER/', home_page,name='home'),
    url(r'^admin/', admin.site.urls),
    url(r'^cucop/', include('apps.contabilidad.urls', namespace="conta")),
    url(r'^focones/', include('apps.focon.urls', namespace="focon")),
    url(r'^pagos/', include('apps.pago.urls', namespace="pago")),
    url(r'^concursos/', include('apps.concurso.urls', namespace="concurso")),
    url(r'', include('registration.backends.default.urls')),

    # url(r'^index/', anidadosviews.index),


]

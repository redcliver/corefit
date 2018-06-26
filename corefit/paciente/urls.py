from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.pacient),
    url(r'^novo', views.novo_pac),
    url(r'^buscar', views.busca_pac),
    url(r'^editar', views.edita_pac),
    ]

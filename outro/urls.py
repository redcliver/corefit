from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.outro),
    url(r'^balanco', views.balanco),
    url(r'^anual', views.anual),
    url(r'^trimestral', views.trimestral),
    url(r'^mensal', views.mensal),
    url(r'^diario', views.diario),
    url(r'^profissionais', views.prof),
    url(r'^novo_prof', views.novo_prof),
    url(r'^editar_prof', views.editar_prof),
    url(r'^salvar', views.salvar),
    ]

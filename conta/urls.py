from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.conta1),
    url(r'^nova', views.nova),
    url(r'^editar', views.editar),
    url(r'^pagar', views.pagar),
    url(r'^salvar', views.salvar),
    ]

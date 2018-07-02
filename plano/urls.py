from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.plano1),
    url(r'^novo', views.novo),
    url(r'^editar', views.editar),
    url(r'^salvar', views.salvar),
    ]

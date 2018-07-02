from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.caixa),
    url(r'^entrada', views.entrada),
    url(r'^retirada', views.retirada),
    url(r'^fechar', views.fechar),
    ]

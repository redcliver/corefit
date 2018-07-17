from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.agenda),
    url(r'^novo', views.novo),
    url(r'^11', views.novo_11),
    url(r'^12', views.novo_12),
    url(r'^13', views.novo_13),
    url(r'^21', views.novo_21),
    url(r'^22', views.novo_22),
    url(r'^23', views.novo_23),
    ]

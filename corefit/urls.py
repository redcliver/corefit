"""
Definition of urls for corefit.
"""

from datetime import datetime
from django.conf.urls import url
import django.contrib.auth.views
from django.contrib.auth.views import login

import app.forms
import app.views

# Uncomment the next lines to enable the admin:
from django.conf.urls import include
#from django.contrib import admin
#admin.autodiscover()

urlpatterns = [
    # Examples:
    url(r'^/$', login, {'template_name': 'home/login.html'}),
    url(r'^home/', include('home.urls')),
    url(r'^presenca/', include('presenca.urls')),
    url(r'^paciente/', include('paciente.urls')),
    url(r'^outros/', include('outro.urls')),
    url(r'^caixa/', include('caixa.urls')),
    url(r'^plano/', include('plano.urls')),
    url(r'^conta/', include('conta.urls')),
    url(r'^agenda/', include('agenda.urls')),
    url(r'^contact$', app.views.contact, name='contact'),
    url(r'^about', app.views.about, name='about'),
    url(r'^login/$',
        django.contrib.auth.views.login,
        {
            'template_name': 'app/login.html',
            'authentication_form': app.forms.BootstrapAuthenticationForm,
            'extra_context':
            {
                'title': 'Log in',
                'year': datetime.now().year,
            }
        },
        name='login'),
    url(r'^logout$',
        django.contrib.auth.views.logout,
        {
            'next_page': '/',
        },
        name='logout'),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    #url(r'^admin/', include(admin.site.urls)),
]

"""dzbank URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from django.contrib import admin
from django.views.generic import TemplateView
from views import *

urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name='index.html')),
    url(r'^import/$', import_depot, name="import-depot"),
    url(r'^import/all/$',
        TemplateView.as_view(template_name='import_all.html'),
        name="import_all"),
    url(r'^ec/$', TemplateView.as_view(template_name='ec.html')),
    url(r'^allocation/$', TemplateView.as_view(template_name='allocation.html')),
    url(r'^stresstest/$', TemplateView.as_view(template_name='stresstest.html')),
    url(r'^performance/$', TemplateView.as_view(template_name='performance.html')),
    url(r'^simulation/$', simulation, name="simulation"),

    url(r'^d/', include('dzbank.urls_data', namespace="d")),
    url(r'^admin/', admin.site.urls),
]

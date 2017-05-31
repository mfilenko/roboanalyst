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
from django.conf.urls import url
from django.contrib import admin
from django.views.generic import TemplateView
from views import *

urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name='index.html')),
    url(r'^import/$', import_depot, name="import-depot"),
    url(r'^data/allocation/portfolio/current/$', current_portfolio_data, name="current-portfolio-data"),
    url(r'^data/allocation/portfolio/conservative/$', conservative_portfolio_data, name="conservative-portfolio-data"),
    url(r'^data/allocation/portfolio/balanced/$', balanced_portfolio_data, name="balanced-portfolio-data"),
    url(r'^data/allocation/portfolio/bold/$', bold_portfolio_data, name="bold-portfolio-data"),
    url(r'^data/simulation/$', simulation_data, name="simulation-data"),
    url(r'^simulation/$', simulation, name="simulation"),
    url(r'^admin/', admin.site.urls),
]

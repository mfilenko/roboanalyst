from django.conf.urls import url
import views

urlpatterns = [
    url(r'^get-accounts/$', views.d_get_accounts, name='get_accounts'),
    url(r'^select-assets/$', views.d_select_assets, name='select_assets')
]

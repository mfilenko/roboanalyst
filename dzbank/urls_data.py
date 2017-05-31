from django.conf.urls import url
import views

urlpatterns = [
    url(r'^figo-connect/$', views.d_figo_connect, name='figo_connect'),
    url(r'^select-assets/$', views.d_select_assets, name='select_assets'),
    url(r'^selected-assets/$',
        views.d_get_selected_assets, name='selected_assets'),
    url(r'^all-assets/$',
        views.d_get_all_assets, name='all_assets')
]

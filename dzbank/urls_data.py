from django.conf.urls import url
import views

urlpatterns = [
    url(r'^get-accounts/$', views.d_get_accounts, name='get_accounts')
]

from django.conf.urls import url
import views

urlpatterns = [
    url(r'^get-accounts/$', views.d_get_accounts, name='get_accounts'),
    url(r'^alloc/portfolio/current/$', views.d_current_portfolio, name="current_portfolio"),
    url(r'^alloc/portfolio/conservative/$', views.d_conservative_portfolio, name="conservative_portfolio_data"),
    url(r'^alloc/portfolio/balanced/$', views.d_balanced_portfolio, name="balanced_portfolio_data"),
    url(r'^alloc/portfolio/bold/$', views.d_bold_portfolio, name="bold_portfolio_data"),
    url(r'^simulation/$', views.d_simulation, name="simulation_data"),
]

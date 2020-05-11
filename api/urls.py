from django.conf.urls import url
from portfolio.views import PortfolioListView, PortfolioView, CustomersListView, CustomersView
from django.urls import path, include

helper_patterns = [
    url(r'^portfolios/$', PortfolioListView.as_view(), name='portfolios'),
    url(r'^portfolios/(?P<pk>[0-9]+)/$', PortfolioView.as_view(), name='get_portfolio'),
    url(r'^customers/$', CustomersListView.as_view(), name='customers'),
    url(r'^customers/(?P<pk>[0-9]+)/$', CustomersView.as_view(), name='get_customer'),
]

urlpatterns = helper_patterns
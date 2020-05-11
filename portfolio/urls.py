from django.conf.urls import url
from portfolio.views import PortfolioListView
from django.urls import path, include

helper_patterns = [
    path('portfolios/', PortfolioListView.as_view(), name='portfolios')
]

urlpatterns = helper_patterns


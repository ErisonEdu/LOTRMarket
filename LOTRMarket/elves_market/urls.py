from django.urls import path
from .views import elven_market_view

urlpatterns = [
    path("elven_market/", elven_market_view, name="home"),
]

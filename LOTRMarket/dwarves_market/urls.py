from django.urls import path
from .views import dwarven_market_view

urlpatterns = [
    path("elven_market/", dwarven_market_view, name="home"),
]
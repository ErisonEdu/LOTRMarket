from django.urls import path
from .views import humans_market_view

urlpatterns = [
    path("human_market/", humans_market_view, name="home"),
]

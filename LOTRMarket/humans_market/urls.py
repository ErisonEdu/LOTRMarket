from django.urls import path
from .views import HumanItemAPIViewSet

urlpatterns = [
    path("human_market/", HumanItemAPIViewSet.as_view, name="humanItems"),
]

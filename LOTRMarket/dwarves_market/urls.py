from django.urls import path
from .views import DwarvenItemAPIViewSet

urlpatterns = [
    path("dwarven_market/", DwarvenItemAPIViewSet.as_view, name="DwarvenItems"),
]

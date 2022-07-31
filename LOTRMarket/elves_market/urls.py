from django.urls import path
from .views import ElvenItemAPIViewSet

urlpatterns = [
    path("elven_market/", ElvenItemAPIViewSet.as_view, name="elvenItems"),
]

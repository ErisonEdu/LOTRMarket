from django import views
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from LOTRMarket.humans_market.views import HumanItemAPIViewSet
from LOTRMarket.elves_market.views import ElvenItemAPIViewSet
from LOTRMarket.dwarves_market.views import DwarvenItemAPIViewSet

router = routers.DefaultRouter()
router.register(r"human_market", HumanItemAPIViewSet),
router.register(r"elven_market", ElvenItemAPIViewSet),
router.register(r'dwarven_market', DwarvenItemAPIViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]


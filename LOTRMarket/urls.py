from django import views
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from LOTRMarket.humans_market.views import HumanItemAPIViewSet

router = routers.DefaultRouter()
router.register(r"human_market", HumanItemAPIViewSet),

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]


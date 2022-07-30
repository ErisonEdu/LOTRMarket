from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path("", include("LOTRMarket.humans_market.urls")),
    path('', include("LOTRMarket.elves_market.urls")),
    path('', include("LOTRMarket.dwarves_market.urls"))
]


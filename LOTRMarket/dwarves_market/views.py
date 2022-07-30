from django.http import HttpResponse

def dwarven_market_view(request):
        return HttpResponse('<h1>Dwarven Market</h1>')
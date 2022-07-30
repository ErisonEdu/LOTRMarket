from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def elven_market_view(request):
        return HttpResponse('<h1>Elven Market</h1>')
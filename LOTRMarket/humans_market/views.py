from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def humans_market_view(request):
        return HttpResponse('<h1>Humans Market</h1>')
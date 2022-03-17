from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def raina(request):
    return HttpResponse('<marquee><h1>Rania is MR.IpL</h1></marquee>')

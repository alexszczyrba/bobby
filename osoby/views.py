from django.http import HttpResponse

def index(request):
    return HttpResponse("kokon mati 24/7")

def about(request):
    return httpResponse("nord.fm")
from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("PUPA")

# Create your views here.

from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import *

# Create your views here.

def primera_vista(request):
    return HttpResponse("Hola Mundo, desde el <b>Curso de Django para profesiones de Daniel Bojorge</b>")

class HomeView(TemplateView):
    template_name = "bases/home.html"
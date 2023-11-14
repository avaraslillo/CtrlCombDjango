from django.shortcuts import render
from django.views.generic import *
from .forms import CustomUserCreationForm
from django.urls import reverse_lazy


class RegistroUsuarioView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("usuarios:login")
    template_name = "usuarios/registro.html"
    

# Create your views here.

from django.shortcuts import render
from django.views.generic import ListView
from .models import Evento

class HomePageView(ListView):
    model = Evento
    template_name = 'app_eventos/home.html'

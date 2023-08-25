from django.shortcuts import redirect, render
from django.views.generic import ListView , DetailView 
from .models import All




class AllList(ListView):
    model = All

class AllDetail(DetailView):
    model = All



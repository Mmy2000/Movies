from django.shortcuts import render
from gendr.models import Category , All
from django.db.models.query_utils import Q
# Create your views here.


def home(request):
    movie_list = All.objects.filter(category__name = 'movie').order_by('-created_at')
    all_list = All.objects.filter().order_by('-created_at')[:6]
    series_list = All.objects.filter(category__name = 'series').order_by('-created_at')[:6]
    cartoon_list = All.objects.filter(category__name = 'cartoon').order_by('-created_at')[:6]
    

    

    return render(request, 'settings/home.html',{
        'movie_list':movie_list,
        'all_list' : all_list,
        'series_list':series_list,
        'cartoon_list':cartoon_list,
        
    })



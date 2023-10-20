from django.urls import path
from .views import AllDetail  , AllList , MovieByTags

app_name = 'gendr'

urlpatterns = [
    path('',AllList.as_view(),name='all_list'),
    path('<slug:slug>',AllDetail.as_view(),name='all_detail'),
    path('tags/<str:slug>',MovieByTags.as_view(),name='movie_by_tags'),
]



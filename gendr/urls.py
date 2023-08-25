from django.urls import path
from .views import AllDetail  , AllList

app_name = 'gendr'

urlpatterns = [
    path('',AllList.as_view(),name='all_list'),
    path('<slug:slug>',AllDetail.as_view(),name='all_detail'),
]


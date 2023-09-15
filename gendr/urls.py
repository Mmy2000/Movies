from django.urls import path
from .views import AllDetail  , AllList , PostByTags

app_name = 'gendr'

urlpatterns = [
    path('',AllList.as_view(),name='all_list'),
    path('<slug:slug>',AllDetail.as_view(),name='all_detail'),
    path('tags/<str:slug>' , PostByTags.as_view() , name='post_by_tags'),

]



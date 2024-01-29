import django_filters
from .models import All

class PropertyFilter(django_filters.FilterSet):
    class Meta:
        model = All
        fields = ['name','category' , 'language' , 'quality']
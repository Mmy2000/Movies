from django import forms

from .models import AddToFavorite

class PropertyFVForm(forms.ModelForm):
    class Meta:
        model = AddToFavorite
        fields = []
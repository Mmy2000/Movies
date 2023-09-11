from django.shortcuts import redirect, render
from django.urls import reverse
from django.views.generic import ListView , DetailView 
from django.views.generic.edit import FormMixin
from .forms import PropertyFVForm
from .filters import PropertyFilter
from django_filters.views import FilterView
from .models import All
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render




class AllList(FilterView):
    model = All
    paginate_by = 9
    filterset_class = PropertyFilter
    template_name = 'gendr/all_list.html'

class AllDetail(FormMixin,DetailView):
    model = All
    form_class = PropertyFVForm


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["related"] = All.objects.filter(category=self.get_object().category).order_by('-created_at')[:3]
        return context
    def post(self , request , *args , **kwargs):
        form = self.get_form()
        if form.is_valid():
            myform = form.save(commit=False)
            myform.gendre= self.get_object()
            myform.user = request.user
            myform.save()

        return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
    






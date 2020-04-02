from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from .models import CovidData
from.forms import CovidDataForm
from django.http import HttpResponse
from .resources import CovidResource

class NewCovidView(CreateView):
    model = CovidData
    form_class = CovidDataForm
    success_url = reverse_lazy('list_forms')
    template_name = 'form_page.html'


class UpdateCovidView(UpdateView):
    model = CovidData
    form_class = CovidDataForm
    template_name = 'form_page.html'
    success_url = reverse_lazy('list_forms')
    pk_url_kwarg = 'covid_pk'

class ListCovidView(ListView):
    model = CovidData
    template_name = 'list_forms.html'
    context_object_name = 'objects'



class DeleteCovidView(DeleteView):
    model = CovidData
    success_url = reverse_lazy('list_forms')
    pk_url_kwarg = 'covid_pk'
    template_name = 'confirm_delete.html'

def export(request):
    covid_resource = CovidResource()
    dataset = covid_resource.export()
    response = HttpResponse(dataset.csv, content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="persons.csv"'
    return response

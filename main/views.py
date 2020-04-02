from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from .models import CovidData
from.forms import CovidDataForm
from django.http import HttpResponse
from .resources import CovidResource
import csv
from django.forms.models import model_to_dict

class NewCovidView(CreateView):
    model = CovidData
    form_class = CovidDataForm
    success_url = reverse_lazy('list_forms')
    template_name = 'new_form.html'


class UpdateCovidView(UpdateView):
    model = CovidData
    form_class = CovidDataForm
    template_name = 'form_page.html'
    success_url = reverse_lazy('list_forms')
    pk_url_kwarg = 'covid_pk'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        qset = list(CovidData.objects.all())
        obj_index = qset.index(context['object'])
        try:
            previous = qset[obj_index - 1]
        except IndexError:
            previous = None
        else:
            previous = previous.id
        try:
            next = qset[obj_index + 1]
        except IndexError:
            next = None
        else:
            next = next.id
        if obj_index == 0:
            previous = None
        context['next_id'] = next
        context['previous_id'] = previous
        return context

class ListCovidView(ListView):
    model = CovidData
    template_name = 'list_forms.html'
    context_object_name = 'objects'



class DeleteCovidView(DeleteView):
    model = CovidData
    success_url = reverse_lazy('list_forms')
    pk_url_kwarg = 'covid_pk'
    template_name = 'confirm_delete.html'

def export(request, covid_id):
    data = model_to_dict(CovidData.objects.get(id=covid_id))
    del data['id']
    keys = [key for key in data.keys()]
    values = [value for value in data.values()]
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = f'attachment; filename="{data["ID_num"]}.csv"'
    writer = csv.writer(response)
    writer.writerow(keys)
    writer.writerow(values)

    return response

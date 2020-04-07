from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from .models import CovidData
from.forms import CovidDataForm
from django.http import HttpResponse
from .resources import CovidResource
import csv
from django.forms.models import model_to_dict
from .forms import SignUpForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Permission
from django.contrib import messages
import datetime
from dal import autocomplete
from django.conf import settings
from django.db.models import Q
import os


def export_file(covid):
    data = model_to_dict(covid)
    
    del data['created_by']
    del data['exported']
    for key, value in data.items():
        if isinstance(value, datetime.date):
            date_string = value.strftime('%d%m%y')
            data[key] = date_string
        if isinstance(value, int):
            data[key] = str(value)
            
        if not value:
            data[key] = ' '
    filename = f"41997.Negifim.{data['result_date']}.{data['id']}.txt"
    del data['id']

    values = [value for value in data.values()]
    content = ';'.join(values)
   
    os.chdir(settings.EXPORT_STRING)
    with open(filename, 'w', encoding='windows-1255') as f:
        f.write(content)
        f.close()
        
        
def index(request):
    if request.user.is_authenticated:
        return redirect('search')
    return render(request, 'index.html')


class DeleteCovidView(DeleteView):
    model = CovidData
    success_url = reverse_lazy('list_forms')
    pk_url_kwarg = 'covid_pk'
    template_name = 'confirm_delete.html'

@login_required
def update_covid(request, covid_id):
    # get id's for next and previous objects if they exist
    covid = CovidData.objects.get(pk=covid_id)
    qset = list(CovidData.objects.all())
    obj_index = qset.index(covid)
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

    if request.method == 'POST':
        form = CovidDataForm(request.POST, instance=covid)
        if form.is_valid():
            tz = form.cleaned_data['ID_num']
            # Validate that if field id_type is 0,1 that its only 9 digits and if it isnt prepend 0's until it is
            if form.cleaned_data['id_type'] in [0,1]:
                while len(tz) < 9:
                    tz = '0' + tz
            data = form.save(commit=False)
            data.ID_num = tz
            data.save()
            return redirect('search')
        for field, error in form.errors.items():
            messages.warning(request, error)
        return redirect('update')
    form = CovidDataForm(instance=covid)
    return render(request, 'form_page.html', {'form': form, 'previous': previous, 'next': next, 'object': covid})

@login_required
def export(request, covid_id):
    covid = CovidData.objects.get(pk=covid_id)
    if covid.exported:
        messages.warning(request, 'הקובץ כבר ייוצא פעם אחת, נא לפנות למנהל המערכת.')
    else:
        export_file(covid)
        covid.exported = True
        covid.save()
        messages.success(request, 'קובץ בדיקה ייוצא בהצלחה')
    return redirect('search')



@login_required
def search_tz(request):
    objects = CovidData.objects.all().order_by('result_date')
    if request.method == 'POST':
        text = request.POST.get('search_tz')
        objects = CovidData.objects.filter(ID_num__icontains=text)
    return render(request, 'search.html', {'objects': objects})

@login_required
def search_date(request):
    objects = None
    if request.method == 'POST':
        date_string = request.POST.get('search_date')
        objects = CovidData.objects.filter(result_date=datetime.datetime.strptime(date_string, '%m/%d/%Y').date())
    return render(request, 'search.html', {'objects': objects})


@login_required
def create_covid(request):
    if request.method == 'POST':
        form = CovidDataForm(request.POST)
        if form.is_valid():
            tz = form.cleaned_data['ID_num']
            # Validate that if field id_type is 0,1 that its only 9 digits and if it isnt prepend 0's until it is
            if form.cleaned_data['id_type'] in [0, 1]:
                while len(tz) < 9:
                    tz = '0' + tz

            # Get data from scanned barcode fields
            result_date_str = form.cleaned_data['plate_details'].split('_')[0]
            result_datetime = datetime.datetime.strptime(result_date_str, '%d-%m-%y')
            sticker_num = rf"{form.cleaned_data['patient_details']}".split('\\')[1]
            data = form.save(commit=False)
            data.created_by = request.user
            data.result_date = result_datetime
            data.sticker_number = sticker_num
            data.ID_num = tz
            # data.result = data.result_test_corona.get_display_value()
            data.save()
            return redirect('search')
        for field, error in form.errors.items():
            messages.warning(request, error)
        return redirect('create')
    form = CovidDataForm()
    return render(request, 'new_form.html', {'form': form})

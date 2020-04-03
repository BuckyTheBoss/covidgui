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
from django.contrib import messages
import datetime

def index(request):
    return render(request, 'index.html')


class NewCovidView(CreateView):
    model = CovidData
    form_class = CovidDataForm
    success_url = reverse_lazy('list_forms')
    template_name = 'new_form.html'

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)


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


@login_required
def export(request, covid_id):
    data = model_to_dict(CovidData.objects.get(id=covid_id))
    del data['id']
    del data['created_by']
    print(data)
    for key, value in data.items():
        if isinstance(value, datetime.date):
            date_string = value.strftime('%d%m%y')
            data[key] = date_string

    values = [str(value) for value in data.values()]

    filename = "my-file.rtf"
    content = ';'.join(values)
    content_1255 = content.encode('windows-1255')
    response = HttpResponse(content_1255, content_type='text/plain')
    response['Content-Disposition'] = f'attachment; filename={filename}'
    return response




def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            key = form.cleaned_data.get('key')
            if key != 'helloworld':
                messages.warning(request, 'קוד הרשמה שגוי, נא לפנות למנהל המערכת')
                return redirect('signup')
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')

            user = authenticate(username=username, password=raw_password)
            login(request, user)
            messages.success(request, 'נרשמת בהצלחה!')
            return redirect('new_form')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

from django import forms
from .models import CovidData


class CovidDataForm(forms.ModelForm):
    class Meta:
        model = CovidData
        fields = '__all__'
        exclude = ['lab_code']


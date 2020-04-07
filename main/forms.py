from django import forms
from .models import CovidData
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from dal import autocomplete


class SignUpForm(UserCreationForm):
    key = forms.CharField(required=True, label='קוד הרשמה', help_text='על מנת לקבל קוד הרשמה נא ליצור קשר עם מנהל המערכת')
    first_name = forms.CharField(required=True, label='שם פרטי')
    last_name = forms.CharField(required=True, label='שם משפחה')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'password1', 'password2', )
        labels = {
            'username': 'שם משתמש',
            'first_name': 'שם פרטי',
            'last_name': 'שם משפחה',
            'password1': 'סיסמא',
            'password2': 'אישור סיסמא',
        }


class CovidDataForm(forms.ModelForm):
    plate_details = forms.CharField(required=False)
    patient_details = forms.CharField(required=False)

    class Meta:
        model = CovidData
        fields = '__all__'
        exclude = ['lab_code', 'lab_desc', 'tested_code', 'year_of_sticker', 'created_by', 'sender_code', 'method_code', 'method_desc', 'spec_code', 'spec_desc', 'result_date', 'sticker_number','result' ]
        labels = {
            'gender': "מין",
            'ID_num': 'ת"ז',
            'first_name': 'שם פרטי',
            'last_name': 'שם משפחה',
            'year_of_birth': 'שנת לידה',
            'internal_code': 'קוד פנימי',
            'internal_number': 'מספר פנימי',
            'section_code': 'קוד מדור מבצע',
            'section_desc': 'תאור מדור מבצע',
            'tested_desc': 'תאור גורם נבדק',
            'take_date': 'תאריך לקיחה',
            'get_date': 'תאריך קבלה',
            'remark': 'הערה',
            'id_type': 'סוג תעודה',
            'sender_name': 'שם גורם שולח',
            'sender_full_name': 'שם גורם שולח מלא',
            'result_test_corona': 'קוד תוצאה'
        }
        widgets = {
            'result_date': forms.DateInput(format="%m/%d/%Y"),
            'remark': forms.Textarea(attrs={'rows': 3, 'cols': 25}),
        }

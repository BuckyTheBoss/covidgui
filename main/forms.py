from django import forms
from .models import CovidData


class CovidDataForm(forms.ModelForm):
    class Meta:
        model = CovidData
        fields = '__all__'
        exclude = ['lab_code', 'lab_desc', 'tested_code', 'year_of_sticker']
        labels = {
            'gender': "מין",
            'ID_num': 'ת"ז',
            'first_name': 'שם פרטי',
            'last_name': 'שם משפחה',
            'year_of_birth': 'שנת לידה',
            'sticker_number': 'מספר מדבקה',
            'internal_code': 'קוד פנימי',
            'internal_number': 'מספר פנימי',
            'spec_code': 'קוד חומר דגימה',
            'spec_desc': 'תאור חומר דגימה',
            'method_code': 'קוד שיטה',
            'method_desc': 'תאור שיטה',
            'section_code': 'קוד מדור מבצע',
            'section_desc': 'תאור מדור מבצע',
            'tested_desc': 'קוד גורם נבדק',
            'take_date': 'תאריך לקיחה',
            'get_date': 'תאריך קבלה',
            'result_date': 'תאריך תוצאה',
            'result': 'תוצאה',
            'remark': 'הערה',
            'id_type': 'סוג תעודה',
            'sender_code': 'קוד גורם שולח',
            'sender_name': 'שם גורם שולח',
            'sender_full_name': 'שם גורם שולח מלא',
            'result_test_corona': 'קוד תוצאה'
        }


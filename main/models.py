from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
import datetime
from django.core.validators import RegexValidator


# Create your models here.


class CovidData(models.Model):
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    lab_code = models.CharField(max_length=5, default='41997')
    lab_desc = models.CharField(max_length=30, default='מעבדת אוניברסיטת תל אביב')
    ID_num = models.CharField(max_length=10, validators=[
            RegexValidator(
                regex='^[0-9]*$',
                message='ת"ז לא תקין - אנא הכנס רק מספרים',
            ),
        ])
    last_name = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    gender = models.CharField(max_length=1, choices=[('ז','זכר'),('נ','נקבה')])
    year_of_birth = models.CharField(max_length=4, choices=[(str(num),str(num)) for num in range(2020,1919,-1)])
    year_of_sticker = models.CharField(max_length=4, default='2020')
    sticker_number = models.CharField(max_length=9)
    internal_code = models.CharField(max_length=2, null=True, blank=True, default='')
    internal_number = models.CharField(max_length=8, null=True, blank=True, default='')
    spec_code = models.CharField(max_length=30, default='RNA')
    spec_desc = models.CharField(max_length=150, default='חומר גנטי')
    method_code = models.CharField(max_length=4, default='qPCR')
    method_desc = models.CharField(max_length=30, default='אמפליפיקציה של חומר גנומי')
    section_code = models.CharField(max_length=4, null=True, blank=True, default='')
    section_desc = models.CharField(max_length=30, null=True, blank=True, default='')
    tested_code = models.CharField(max_length=9, default="259")
    tested_desc = models.CharField(max_length=30)
    take_date = models.DateField()
    get_date = models.DateField()
    result_date = models.DateField(default=timezone.now())
    result = models.CharField(max_length=30, null=True, default='', blank=True)
    remark = models.TextField(max_length=2000, default='', blank=True)
    id_type = models.IntegerField(choices=[(0,'ת"ז ישראלי - 0'),(1, 'ת"ז ישראלי - 1'),(2, 'דרכון - 2'),(3, 'אחר - 3')])
    sender_code = models.IntegerField(default=0)
    sender_name = models.CharField(max_length=30, null=True, blank=True, default='')
    sender_full_name = models.CharField(max_length=100, null=True, blank=True, default='')
    result_test_corona = models.IntegerField(choices=[(1,'חיובי'), (0,'שלילי'), (2,'בעבודה'), (999,'לא בוצע')])
    exported = models.BooleanField(default=False)

    class Meta:
        ordering = ['-id']


    def __str__(self):
        return f'ID: {self.ID_num} Result date:{self.result_date}'
    

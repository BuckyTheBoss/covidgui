from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class TZ(models.Model):
    num = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return self.num


class CovidData(models.Model):
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True )
    lab_code = models.CharField(max_length=5, default='41997')
    lab_desc = models.CharField(max_length=30, default='מעבדת אוניברסיטת תל אביב')
    ID_num = models.ForeignKey(TZ, on_delete=models.CASCADE)
    last_name = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    gender = models.CharField(max_length=1, choices=[('ז','זכר'),('נ','נקבה')])
    year_of_birth = models.CharField(max_length=4)
    year_of_sticker = models.CharField(max_length=4, default='2020')
    sticker_number = models.CharField(max_length=9)
    internal_code = models.CharField(max_length=2, null=True, blank=True, default=' ')
    internal_number = models.CharField(max_length=8, null=True, blank=True, default=' ')
    spec_code = models.CharField(max_length=30)
    spec_desc = models.CharField(max_length=150)
    method_code = models.CharField(max_length=4)
    method_desc = models.CharField(max_length=30)
    section_code = models.CharField(max_length=4, null=True, blank=True, default=' ')
    section_desc = models.CharField(max_length=30, null=True, blank=True, default=' ')
    tested_code = models.CharField(max_length=9, default="259")
    tested_desc = models.CharField(max_length=30)
    take_date = models.DateField()
    get_date = models.DateField()
    result_date = models.DateField()
    result = models.CharField(max_length=30)
    remark = models.TextField(max_length=2000, default='', blank=True)
    id_type = models.IntegerField(choices=[(0,'ת"ז ישראלי - 0'),(1, 'ת"ז ישראלי - 1'),(2, 'דרכון - 2'),(3, 'אחר - 3')])
    sender_code = models.IntegerField(default=0)
    sender_name = models.CharField(max_length=30, null=True, blank=True, default=' ')
    sender_full_name = models.CharField(max_length=100, null=True, blank=True, default=' ')
    result_test_corona = models.IntegerField(choices=[(1,'חיובי'), (0,'שלילי'), (2,'בעבודה'), (999,'לא בוצע')])

    def __str__(self):
        return f'ID: {self.ID_num} Result date:{self.result_date}'
    

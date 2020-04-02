from django.db import models

# Create your models here.


class CovidData(models.Model):
    lab_code = models.CharField(max_length=5, default='41997')
    lab_desc = models.CharField(max_length=30, default='מעבדת אוניברסיטת תל אביב')
    tested_code = models.CharField(max_length=9, default=259)
    year_of_sticker = models.CharField(max_length=4, default='2020')
    gender = models.CharField(max_length=1, choices=[('ז','זכר'),('נ','נקבה')])
    ID_num = models.CharField(max_length=10)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    year_of_birth = models.CharField(max_length=4)
    sticker_number = models.CharField(max_length=9)
    internal_code = models.CharField(max_length=2, null=True)
    internal_number = models.CharField(max_length=8, null=True)
    spec_code = models.CharField(max_length=30)
    spec_desc = models.CharField(max_length=150)
    method_code = models.CharField(max_length=4)
    method_desc = models.CharField(max_length=30)
    section_code = models.CharField(max_length=4, null=True)
    section_desc = models.CharField(max_length=30, null=True)
    tested_desc = models.CharField(max_length=30)
    take_date = models.DateField()
    get_date = models.DateField()
    result_date = models.DateField()
    result = models.CharField(max_length=30)
    remark = models.CharField(max_length=2000, default='')
    id_type = models.IntegerField(choices=[(0,'ת"ז ישראלי - 0'),(1, 'ת"ז ישראלי - 1'),(2, 'דרכון - 2'),(3, 'אחר - 3')])
    sender_code = models.IntegerField(default=0)
    sender_name = models.CharField(max_length=30, null=True)
    sender_full_name = models.CharField(max_length=100, null=True)
    result_test_corona = models.IntegerField(choices=[(1,'חיובי'), (0,'שלילי'), (2,'בעבודה'), (999,'לא בוצע')])
    
    

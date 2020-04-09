from django.contrib import admin
from .models import CovidData
# Register your models here.

class CovidDataAdmin(admin.ModelAdmin):
    list_display = ('ID_num', 'created_by', 'sticker_number', 'exported', 'result_test_corona')
    search_fields = ['ID_num', 'sticker_number']

admin.site.register(CovidData, CovidDataAdmin)

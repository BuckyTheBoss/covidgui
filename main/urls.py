from django.urls import path
from . import  views

urlpatterns = [
    path('new_form/', views.NewCovidView.as_view(), name='new_form'),
    path('', views.ListCovidView.as_view(), name='list_forms'),
    path('edit_form/<int:covid_pk>', views.UpdateCovidView.as_view(), name='edit_form'),
    path('delete_form/<int:covid_pk>', views.DeleteCovidView.as_view(), name='delete_form'),
    path('export/<int:covid_id>', views.export, name='export'),
]

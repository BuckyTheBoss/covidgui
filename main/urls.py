from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('new_form/', views.create_covid, name='create'),
    path('edit_form/<int:covid_id>', views.update_covid, name='update'),
    path('delete_form/<int:covid_pk>', login_required(views.DeleteCovidView.as_view()), name='delete_form'),
    path('export/<int:covid_id>', views.export, name='export'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), {'next_page': '/'}, name='logout'),
    path('', views.index, name='homepage'),
    path('search', views.search_tz, name='search'),
    path('search_date', views.search_date, name='search_date'),

]

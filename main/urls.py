from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('new_form/', login_required(views.NewCovidView.as_view()), name='new_form'),
    path('list/', login_required(views.ListCovidView.as_view()), name='list_forms'),
    path('edit_form/<int:covid_pk>', login_required(views.UpdateCovidView.as_view()), name='edit_form'),
    path('delete_form/<int:covid_pk>', login_required(views.DeleteCovidView.as_view()), name='delete_form'),
    path('export/<int:covid_id>', views.export, name='export'),
    path('signup/', views.signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), {'next_page': '/'}, name='logout'),
    path('', views.index, name='homepage')
]

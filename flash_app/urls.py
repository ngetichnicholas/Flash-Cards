from django.conf.urls import url
from django.urls import re_path,path,include
from django.contrib.auth import views as auth_views
from . import views as app_views
from rest_framework.authtoken.views import obtain_auth_token


urlpatterns = [
  path('',app_views.index,name='home'),
  path('accounts/register/',app_views.register,name='register'),
  path('accounts/login/',app_views.login,name='login'),
  path('logout/',auth_views.LogoutView.as_view(template_name = 'registration/logout.html'),name='logout'),
  path('accounts/profile/',app_views.profile,name='profile'),
]
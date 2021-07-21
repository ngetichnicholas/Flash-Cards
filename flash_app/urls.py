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
  path('create_flashcard/',app_views.create_card,name='create_card'),
  path('card/<int:card_id>',app_views.card_view,  name='card_view'),
  path('update/<int:card_id>',app_views.update_card,name='update_card'),
  path('api/flashcards/',app_views.FlashCardList.as_view()),
  path('api/subjects/',app_views.SubjectList.as_view()),
  path('api_token/', obtain_auth_token),
  path('delete_card/<card_id>',app_views.delete_card,name='delete_card'),
  path('api/card/<int:pk>',app_views.FlashCardActions.as_view()),
  path('physics/',app_views.filter_physics_cards,name='physics'),
  path('bio/',app_views.filter_bio_cards,name='bio'),
  path('history/',app_views.filter_history_cards,name='history'),
  path('chem/',app_views.filter_chem_cards,name='chem'),

]
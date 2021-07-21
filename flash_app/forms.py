from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import FlashCard
    
class Registration(UserCreationForm):
  email = forms.EmailField()

  class Meta:
    model = User
    fields = ['username','email','password1','password2']

class CreateCardForm(forms.ModelForm):

	class Meta:
		model = FlashCard
		fields = ['title','subject', 'front_side', 'back_side']

class UpdateCardForm(forms.ModelForm):
  class Meta:
    model = FlashCard
    fields = ['title','subject','front_side','back_side']
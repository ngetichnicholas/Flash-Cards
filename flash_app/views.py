from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import FlashCard
from django.contrib.auth import authenticate, login
from django.contrib.auth import login as auth_login
from . forms import Registration
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib import messages



# Create your views here.
def index(request):
  current_user = request.user
  user_cards = FlashCard.objects.filter(user_id = current_user.id).all().order_by('-created_at')

  return render (request,'index.html',{"current_user":current_user, "user_cards":user_cards})

def register(request):
  if request.method == 'POST':
    form = Registration(request.POST)
    if form.is_valid():
      form.save()
      email = form.cleaned_data['email']
      username = form.cleaned_data.get('username')

      messages.success(request,f'Account for {username} created,you can now login')
      return redirect('login')
  else:
    form = Registration()
  return render(request,'registration/registration_form.html',{"form":form})

def login(request):
  if request.method == 'POST':
    form = AuthenticationForm(request=request, data=request.POST)
    if form.is_valid():
      username = form.cleaned_data.get('username')
      password = form.cleaned_data.get('password')
      user = authenticate(username=username, password=password)
      if user is not None:
        auth_login(request, user)
        messages.info(request, f"You are now logged in as {username}")
        return redirect('home')
      else:
        messages.error(request, "Invalid username or password.")
    else:
      messages.error(request, "Invalid username or password.")
  form = AuthenticationForm()
  return render(request = request,template_name = "registration/login.html",context={"form":form})

@login_required
def profile(request):
  current_user = request.user  
  return render(request,'profile/profile.html',{"current_user":current_user})

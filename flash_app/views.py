from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import FlashCard
from django.contrib.auth import authenticate, login
from django.contrib.auth import login as auth_login
from . forms import Registration,CreateCardForm,UpdateCardForm
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib import messages
from django.http import HttpResponse, Http404,HttpResponseRedirect
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import  Subject,FlashCard
from .serializer import FlashCardSerializer,SubjectSerializer
from rest_framework import status
from rest_framework import viewsets
from .permissions import IsAdminOrReadOnly
from django.core.exceptions import ObjectDoesNotExist


# Create your views here.
@login_required
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

@login_required
def create_card(request):
  if request.method == 'POST':
    new_card_form = CreateCardForm(request.POST,request.FILES) 
    if new_card_form.is_valid():
      new_card = new_card_form.save(commit = False)
      new_card.user = request.user
      new_card.save()
      return redirect('home')

  else:
    new_card_form = CreateCardForm()
  return render(request,'create_card.html',{"new_card_form":new_card_form})

def card_view(request,card_id):
  current_user = request.user
  user_cards = FlashCard.objects.filter(user_id = current_user.id).all().order_by('-created_at')
  card = FlashCard.objects.get(pk = card_id)
  
  return render(request, 'card_page.html', {'current_user':current_user,'user_cards':user_cards,'card':card})

@login_required
def delete_card(request,card_id):
  current_user = request.user
  card = FlashCard.objects.get(pk=card_id)
  if card:
    card.delete_card()
  return redirect('home')

@login_required
def update_card(request, card_id):
  card = FlashCard.objects.get(pk=card_id)
  if request.method == 'POST':
    update_card_form = UpdateCardForm(request.POST, instance=card)
    if update_card_form.is_valid():
      update_card_form.save()
      messages.success(request, f'Flashcard updated!')
      return redirect('home')
  else:
    update_card_form = UpdateCardForm(instance=card)

  return render(request, 'update_card.html', {"update_card_form":update_card_form})

#API Views
class FlashCardList(APIView):
  def get(self,request,format=None):
    projects=FlashCard.objects.all()
    serializers=FlashCardSerializer(projects,many=True)
    return Response(serializers.data)

  def post(self, request, format=None):
    serializers = FlashCardSerializer(data=request.data)
    if serializers.is_valid():
        serializers.save()
        return Response(serializers.data, status=status.HTTP_201_CREATED)
    return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

  permission_classes = (IsAdminOrReadOnly,)

class SubjectList(APIView):
  def get(self,request,format=None):
    profiles=Subject.objects.all()
    serializers=SubjectSerializer(profiles,many=True)
    return Response(serializers.data)

class FlashCardActions(APIView):
  permission_classes = (IsAdminOrReadOnly,)
  def get_card(self, pk):
    try:
      return FlashCard.objects.get(pk=pk)
    except FlashCard.DoesNotExist:
      return Http404

  def get(self, request, pk, format=None):
    card = self.get_card(pk)
    serializers = FlashCardSerializer(card)
    return Response(serializers.data)

  def put(self, request, pk, format=None):
    card = self.get_card(pk)
    serializers = FlashCardSerializer(card, request.data)
    if serializers.is_valid():
      serializers.save()
      return Response(serializers.data)
    else:
      return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

  def delete(self, request, pk, format=None):
    card = self.get_card(pk)
    card.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

def filter_physics_cards(request):
  try:
   cards = FlashCard.objects.filter(subject =1)
  except ObjectDoesNotExist:
    raise Http404()
  return render(request, 'subjects.html', {'cards':cards})

def filter_bio_cards(request):
  try:
   cards = FlashCard.objects.filter(subject =2)
  except ObjectDoesNotExist:
    raise Http404()
  return render(request, 'subjects.html', {'cards':cards})

def filter_history_cards(request):
  try:
   cards = FlashCard.objects.filter(subject =3)
  except ObjectDoesNotExist:
    raise Http404()
  return render(request, 'subjects.html', {'cards':cards})

def filter_chem_cards(request):
  try:
   cards = FlashCard.objects.filter(subject =4)
  except ObjectDoesNotExist:
    raise Http404()
  return render(request, 'subjects.html', {'cards':cards})

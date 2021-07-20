from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Card


# Create your views here.
def index(request):
  cards = Card.show_cards()

  return render (request,'index.html',{"cards":cards})

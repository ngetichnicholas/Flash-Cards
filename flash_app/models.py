from django.db import models

# Create your models here.
class Card(models.Model):
  pass

  @classmethod
  def show_cards(cls):
    cards = cls.objects.all()
    return cards

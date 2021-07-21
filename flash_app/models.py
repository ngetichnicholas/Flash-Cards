from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Card(models.Model):
  title = models.CharField(max_length=144)
  subject = models.CharField(max_length=50)
  front_side = models.TextField()
  back_side = models.TextField()
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField()
  user = models.ForeignKey(User, on_delete=models.CASCADE)

  def __str__(self):
    return self.title

  @classmethod
  def show_cards(cls):
    cards = cls.objects.all()
    return cards



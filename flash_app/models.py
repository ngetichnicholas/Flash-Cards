from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class FlashCard(models.Model):
  title = models.CharField(max_length=144)
  subject = models.CharField(max_length=50)
  front_side = models.TextField()
  back_side = models.TextField()
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField()
  user = models.ForeignKey(User, on_delete=models.CASCADE)

  def save_card(self):
    self.save()

  def delete_card(self):
    self.delete()

  def __str__(self):
    return self.title

  @classmethod
  def show_cards(cls):
    cards = cls.objects.all()
    return cards



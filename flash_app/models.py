from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Subject(models.Model):
  name = models.CharField(max_length=50)

  def save_subject(self):
    self.save()

  def delete_subject(self):
      self.delete()

  def update_subject(self, update):
    self.name = update
    self.save()

  @classmethod
  def get_subject_id(cls, id):
    subject_id = Subject.objects.get(pk = id)
    return subject_id

  def __str__(self):
    return self.name

class FlashCard(models.Model):
  title = models.CharField(max_length=144)
  subject = models.ForeignKey(Subject,on_delete=models.CASCADE)
  front_side = models.TextField()
  back_side = models.TextField()
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  user = models.ForeignKey(User, on_delete=models.CASCADE)

  def save_card(self):
    self.save()

  def delete_card(self):
    self.delete()

  @classmethod
  def search_cards(cls, title):
    return cls.objects.filter(title__icontains=title).all()

  @classmethod
  def show_cards(cls):
    cards = cls.objects.all()
    return cards

  def __str__(self):
    return self.title





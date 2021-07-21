from rest_framework import serializers
from .models import FlashCard, Subject


class FlashCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = FlashCard
        fields = ['id','title', 'subject', 'front_side', 'back_side','created_at','updated_at']


class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = ['id', 'name']


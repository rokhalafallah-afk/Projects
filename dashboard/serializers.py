# dashboard/serializers.py
from rest_framework import serializers
from .models import Registration, User, Event, News, Match  # عدلي حسب أسماء الـ Models عندك


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'

class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = '__all__'

class SportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Match
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Registration
        fields = '__all__'
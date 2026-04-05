# dashboard/serializers.py
from rest_framework import serializers
<<<<<<< HEAD
from .models import Registration, User, Event, News, Match  # عدلي حسب أسماء الـ Models عندك
=======
from .models import User, Event, News, Match  # عدلي حسب أسماء الـ Models عندك
>>>>>>> 3bb2af9d2b9fd6069068d29d584b95000576f7b2


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
<<<<<<< HEAD

class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Registration
        fields = '__all__'
=======
>>>>>>> 3bb2af9d2b9fd6069068d29d584b95000576f7b2

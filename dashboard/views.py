from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from rest_framework import viewsets
from .models import News, Event, Match, User, Registration
from .serializers import NewsSerializer, UserSerializer, EventSerializer, SportSerializer, RegistrationSerializer
from .models import User, Event , News, Match
from .serializers import UserSerializer
from django.shortcuts import redirect
# Create your views here.

# dashboard/views.py

def home(request):
    return redirect("/admin/login/")
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class NewsViewSet(viewsets.ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer

class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    
class SportViewSet(viewsets.ModelViewSet):
    queryset = Match.objects.all()
    serializer_class = SportSerializer

class RegistrationViewSet(viewsets.ModelViewSet):
    queryset = Registration.objects.all()
    serializer_class = RegistrationSerializer
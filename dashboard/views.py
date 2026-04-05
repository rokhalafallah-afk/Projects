from django.shortcuts import render, redirect
from django.http import HttpResponse
from rest_framework import viewsets
from .models import News, Event, Match, User, Registration
from .serializers import NewsSerializer, UserSerializer, EventSerializer, SportSerializer, RegistrationSerializer

# ── Page views ────────────────────────────────────────────────────────────────

def home(request):
    news = News.objects.order_by('-date')[:6]
    events = Event.objects.order_by('date')[:4]
    matches = Match.objects.order_by('match_date')[:4]
    return render(request, 'index.html', {'news': news, 'events': events, 'matches': matches})

def achiv_news(request):
    news = News.objects.order_by('-date')
    return render(request, 'achiv-news.html', {'news': news})

def conferences(request):
    events = Event.objects.order_by('date')
    return render(request, 'confernces.html', {'events': events})

def seminars(request):
    events = Event.objects.order_by('date')
    return render(request, 'seminars.html', {'events': events})

def month(request):
    events = Event.objects.order_by('date')
    return render(request, 'month.html', {'events': events})

def week_events(request):
    events = Event.objects.order_by('date')
    return render(request, 'weekEvents.html', {'events': events})

def workshops(request):
    events = Event.objects.order_by('date')
    return render(request, 'workShops.html', {'events': events})

def student_news(request):
    return render(request, 'student-new.html')

def top_news(request):
    return render(request, 'top-new.html')

def service_portal(request):
    return render(request, 'serviceportal.html')

def form_club(request):
    matches = Match.objects.filter(status='upcoming').order_by('match_date')
    return render(request, 'form club.html', {'matches': matches})

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
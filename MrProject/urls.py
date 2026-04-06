"""
URL configuration for MrProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from dashboard import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('dashboard.urls')),

    # Page routes
    path('', views.home, name='index'),
    path('achiv-news/', views.achiv_news, name='achiv-news'),
    path('conferences/', views.conferences, name='conferences'),
    path('seminars/', views.seminars, name='seminars'),
    path('month/', views.month, name='month'),
    path('week-events/', views.week_events, name='week-events'),
    path('workshops/', views.workshops, name='workshops'),
    path('student-news/', views.student_news, name='student-news'),
    path('top-news/', views.top_news, name='top-news'),
    path('service-portal/', views.service_portal, name='service-portal'),
    path('form-club/', views.form_club, name='form-club'),
]




from rest_framework.routers import DefaultRouter
from django.views.generic import TemplateView
from django.urls import path, include
from .views import UserViewSet, NewsViewSet, EventViewSet, SportViewSet, RegistrationViewSet
from django.views.generic import TemplateView, RedirectView

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'news', NewsViewSet)
router.register(r'events', EventViewSet)
router.register(r'sports', SportViewSet)
router.register(r'registrations', RegistrationViewSet)  


urlpatterns = [
]

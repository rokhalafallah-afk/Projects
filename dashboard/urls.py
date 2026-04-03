from rest_framework.routers import DefaultRouter
from django.views.generic import TemplateView
from django.urls import path, include
from .views import UserViewSet, NewsViewSet, EventViewSet, SportViewSet
from django.views.generic import TemplateView, RedirectView

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'news', NewsViewSet)
router.register(r'events', EventViewSet)
router.register(r'sports', SportViewSet)

urlpatterns = [
    # API routes
    path('', include(router.urls)),

]

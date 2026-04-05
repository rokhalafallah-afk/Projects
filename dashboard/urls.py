from rest_framework.routers import DefaultRouter
from django.views.generic import TemplateView
from django.urls import path, include
<<<<<<< HEAD
from .views import UserViewSet, NewsViewSet, EventViewSet, SportViewSet, RegistrationViewSet
=======
from .views import UserViewSet, NewsViewSet, EventViewSet, SportViewSet
>>>>>>> 3bb2af9d2b9fd6069068d29d584b95000576f7b2
from django.views.generic import TemplateView, RedirectView

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'news', NewsViewSet)
router.register(r'events', EventViewSet)
router.register(r'sports', SportViewSet)
<<<<<<< HEAD
router.register(r'registrations', RegistrationViewSet)  
=======

>>>>>>> 3bb2af9d2b9fd6069068d29d584b95000576f7b2
urlpatterns = [
    # API routes
    path('', include(router.urls)),

]

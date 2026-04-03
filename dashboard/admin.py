from django.contrib import admin

from .models import News, Event, Match

admin.site.register(News)
admin.site.register(Event)
admin.site.register(Match)
# Register your models here.

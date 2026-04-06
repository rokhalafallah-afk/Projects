from django.contrib import admin

from .models import News, Event, Match,User, Registration

admin.site.register(News)
admin.site.register(Event)
admin.site.register(Match)
admin.site.register(User)
admin.site.register(Registration)
# Register your models here.

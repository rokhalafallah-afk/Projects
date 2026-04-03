from django.db import models

from django.db import models

class News(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateTimeField()

    def __str__(self):
        return self.title
    
class Match(models.Model):
    team1 = models.CharField(max_length=100)
    team2 = models.CharField(max_length=100)
    match_date = models.DateTimeField()
    location = models.CharField(max_length=200)
    score = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return f"{self.team1} vs {self.team2}" 
    
class User(models.Model):
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(blank=True, null=True)
    is_active = models.BooleanField(default=True)  # لو المستخدم مفعل أو لا
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username
# Create your models here.

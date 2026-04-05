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
    STATUS_CHOICES=[
        ('upcoming', 'Upcoming'),
        ('ongoing', 'Ongoing'),
        ('finished', 'Finished')]

    team1 = models.CharField(max_length=100)
    team2 = models.CharField(max_length=100)
    match_date = models.DateTimeField()
    location = models.CharField(max_length=200)
    score = models.CharField(max_length=20, blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='upcoming') #ADD STATUS FIELD
    def __str__(self):
        return f"{self.team1} vs {self.team2}" 
    
class User(models.Model):
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(blank=True, null=True)
    is_active = models.BooleanField(default=True)  # لو المستخدم مفعل أو لا
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username
    
class Registration(models.Model):
    full_name = models.CharField(max_length=150)
    university_id = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=20)
    match = models.ForeignKey(Match, on_delete=models.CASCADE, related_name='registrations')
    registered_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.full_name} -> {self.match}"

    class Meta:
        # Prevents same university_id from registering for the same match twice
        unique_together = ['university_id', 'match']

# Create your models here.

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=200)
    description=models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=False)
    def __str__(self):
        return self.title
    
class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    bio = models.CharField(max_length=500,blank=True)
    location = models.CharField(max_length=100,blank=True)
    profile_picture = models.ImageField(upload_to='profile_pics/',blank=True)

    def __str__(self):
        return f"{self.user.username}'s Profile" 
    

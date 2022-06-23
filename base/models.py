from distutils.command.upload import upload
from email.policy import default
from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    body = models.TextField(max_length=2000)
    likes = models.IntegerField(default=0)
    image = models.ImageField(upload_to='post_images', null =True, blank = True)
    
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    firstName = models.TextField(max_length=100)
    lastName = models.TextField(max_length=100)
    location = models.TextField(max_length=200)
    cover = models.ImageField(upload_to='cover_images', null=True, blank= True, max_length=2000)
    avatar = models.ImageField(upload_to ='profile_images',null=True, blank= True,max_length=2000)
    bio = models.TextField(max_length=2000)
    birthday = models.DateField()
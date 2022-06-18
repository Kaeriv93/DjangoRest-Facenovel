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
    cover = models.ImageField(upload_to='cover_images', null=True, blank= True, default='https://ga-shop-production-herokuapp-com.global.ssl.fastly.net/assets/images/logo_1200_by_627_1QIVL.jpg', max_length=2000)
    avatar = models.ImageField(upload_to ='profile_images', default='https://as1.ftcdn.net/v2/jpg/03/53/11/00/1000_F_353110097_nbpmfn9iHlxef4EDIhXB1tdTD0lcWhG9.jpg',null=True, blank= True,max_length=2000)
    bio = models.TextField(max_length=2000)
    birthday = models.DateField()
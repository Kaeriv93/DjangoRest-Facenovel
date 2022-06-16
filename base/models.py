from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    body = models.TextField(max_length=2000)
    likes = models.IntegerField(default=0)
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework import permissions
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework import status


from .serializers import PostSerializer, ProfileSerializer, UserSerializer
from base.models import Post, Profile

from base.apiroute import serializers

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['username'] = user.username
        token['firstname'] = user.first_name
        token['lastname'] = user.last_name
        # ...

        return token

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

@api_view(['GET','PUT','POST','DELETE'])
def getRoutes(request):
    routes =[
        '/api/token',
        '/api/token/refresh'
    ]
    return Response(routes)

@api_view(['GET','PUT','POST','DELETE'])
def getPosts(request):
    posts = Post.objects.all()
    serializer = PostSerializer(posts, many = True)
    return Response(serializer.data)


@api_view(['GET','PUT','POST','DELETE'])
def getUsers(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many = True)
    return Response(serializer.data)

@api_view(['GET','PUT','POST','DELETE'])
def getProfiles(request):
    profiles = Profile.objects.all()
    serializer = ProfileSerializer(profiles, many = True)
    return Response(serializer.data)
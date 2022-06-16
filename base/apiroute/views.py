from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework import status


from .serializers import PostSerializer
from base.models import Post, Profile

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
    parser_classes = (MultiPartParser, FormParser)
    posts = Post.objects.all()
    serializer = PostSerializer(posts, many = True)
    return Response(serializer.data)
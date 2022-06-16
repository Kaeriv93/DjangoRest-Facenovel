from dataclasses import fields
from rest_framework.serializers import ModelSerializer
from base.models import Post, Profile

class PostSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'
        
class Profile(ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'
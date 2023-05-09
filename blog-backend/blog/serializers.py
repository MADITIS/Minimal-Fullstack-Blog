from rest_framework import serializers
from .models import Blog
from django.contrib.auth import get_user_model
from user.serializers import UserSerializer

class BlogSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)
    class Meta:
        model = Blog
        fields = '__all__'

class CreateBlogSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)
    class Meta:
        model = Blog
        fields = ('title', 'content', 'image', 'author')
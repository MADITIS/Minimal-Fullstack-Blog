from msilib import datasizemask
from urllib import response
from .models import User

from django.contrib.auth import authenticate
from rest_framework import status
from backend.response import _Response
from rest_framework.views import APIView
from user.serializers import UserSerializer, CreateSerializer, LoginSerializer
from rest_framework_simplejwt.tokens import RefreshToken

class UsersView(APIView):
    def get(self, request, *args, **kwargs):
        model_data = User.objects.filter().all()
        serializer_context = {
            'request': request,
        }
        if model_data:
            data = UserSerializer(model_data, many=True, context=serializer_context).data
            return _Response(data, status=status.HTTP_200_OK, message="The request was successful.")
        return _Response(status=status.HTTP_204_NO_CONTENT, message="Item Does not exist")

class UserView(APIView):
    def get(self, request, *args, **kwargs):
        pk = kwargs.get("pk", "")

        try:
            user = User.objects.filter(is_superuser=False).get(pk=pk)
        except User.DoesNotExist:
            return _Response(status=status.HTTP_400_BAD_REQUEST, message="Invalid Id")

        user_data = UserSerializer(user).data
        return _Response(user_data, status=status.HTTP_200_OK, message="The request was successful.")

class CreateUserView(APIView):
    def post(self, request, *args, **kwargs):
        post_data = request.data
        username, email = post_data.get("username"), post_data.get("email")
        isEmail = User.objects.filter(email=email).exists()
        if isEmail:
            return _Response(post_data, status=status.HTTP_409_CONFLICT, message="email already exists")
        serializer = CreateSerializer(data=post_data)
        if serializer.is_valid():
            serializer.save()
            return _Response(post_data, status=status.HTTP_201_CREATED, message="The request was successful.")
        return _Response(data=post_data,status=status.HTTP_400_BAD_REQUEST, message="Invalid Data")

    def get(self, request, *args, **kwargs):
        print("get")
        return _Response(status=status.HTTP_405_METHOD_NOT_ALLOWED, message="Create User using Post")
    

class DeleteUserView(APIView):
    def post(self, request, *args, **kwargs):
        user_id = request.data.get("user_id")
        if not user_id:
            return _Response(status=status.HTTP_400_BAD_REQUEST, message="Invalid User ID")
        try:
            user = User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return _Response(status=status.HTTP_404_NOT_FOUND, message="User not found")

        user.delete()
        return _Response(data=user_id)
    def get(self, request, *args, **kwargs):
        return _Response(status=status.HTTP_405_METHOD_NOT_ALLOWED, message="Delete User using Post")


class LoginUser(APIView):
    def post(self, request):
        data = request.data
        email, password = data.get("email"), data.get("password")
        print("email:", email, "password:", password)
        temp = User.objects.filter(email=email)
        print(temp, "is user")

        user = authenticate(request, email=email, password=password)
        print("user", user)
        if user:
            refresh = RefreshToken.for_user(user)
            tokens = {
                "access":str(refresh.access_token),
                "refresh": str(refresh)
            }
            response_data = {
                "user": UserSerializer(user).data,
                "tokens": tokens,
            }
            return _Response(data=response_data,status=status.HTTP_200_OK, message="Request successful")
        return _Response(status=status.HTTP_404_NOT_FOUND, message="User Not Found")


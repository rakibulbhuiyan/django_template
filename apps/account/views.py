from django.shortcuts import render
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate, login

from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView


from .serializers import (
    UserCreateSerializer
)
User = get_user_model()


class UserSignupView(generics.CreateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = UserCreateSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        response_data = {
            "code": status.HTTP_201_CREATED,
            "message": "User created successfully",
            "data": user.serialize()
        }
        return Response(response_data, status=status.HTTP_201_CREATED)


class UserLoginView(APIView):
    permission_classes = ('IsAuthenticated',)

    def post(self, request, *args, **kwargs):
        email = request.data.get('email')
        password = request.data.get('password')
        user = authenticate(email=email, password=password)
        if user is not None:
            login(request, user)
            response_data = {
                "code": status.HTTP_200_OK,
                "message": "User logged in successfully",
                "data": user.serialize()
            }
            return Response(response_data, status=status.HTTP_200_OK)
        else:
            response_data = {
                "code": status.HTTP_400_BAD_REQUEST,
                "message": "Invalid credentials",
                "data": None
            }
            return Response(response_data, status=status.HTTP_400_BAD_REQUEST)

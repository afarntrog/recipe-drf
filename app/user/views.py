from django.shortcuts import render
from user.serializers import UserSerializer, AuthTokenSerializer
from rest_framework import generics
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings

class CreateUserView(generics.CreateAPIView):
    serializer_class = UserSerializer


class CreateTokeView(ObtainAuthToken):
    """Create auth toke for user"""
    serializer_class = AuthTokenSerializer
    renderer_classes =  api_settings.DEFAULT_RENDERER_CLASSES

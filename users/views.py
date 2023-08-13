import json
from django.contrib.auth import authenticate, login
from django.contrib.auth.hashers import make_password, check_password
from django.http import HttpRequest
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import UserRegistrationSerializer, UserLoginSerializer
from .models import User


@api_view(["GET"])
def api_home(request, *args, **kwargs):
    return Response({"message": "I'm Alive!"})


@api_view(["POST"])
def api_register_user(request: HttpRequest, *args, **kwargs):
    serializer = UserRegistrationSerializer(data=json.loads(request.body))
    if serializer.is_valid():
        username = serializer.validated_data['username']
        password = serializer.validated_data['password']
        email = serializer.validated_data['email']
        subscription_status = serializer.validated_data['subscription_status']

        user = User.objects.create(username=username,
                                   password=make_password(password),
                                   email=email,
                                   subscription_status=subscription_status)

        return Response({"message": "User registered successfully"}, status=201)
    return Response(serializer.errors, status=400)


@api_view(["POST"])
def api_login_user(request: HttpRequest, *args, **kwargs):
    serializer = UserLoginSerializer(data=json.loads(request.body))
    if serializer.is_valid():
        username = serializer.validated_data['username']
        password = serializer.validated_data['password']
        user = User.objects.filter(username=username).first()
        user_found = user is not None
        if user_found and check_password(password, user.password):
            return Response({"message": "Login successful"}, status=200)
        return Response({"message": "Invalid credentials"}, status=401)
    return Response(serializer.errors, status=400)

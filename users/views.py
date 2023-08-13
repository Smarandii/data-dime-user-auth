from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User as DjangoUser
from django.contrib.auth.hashers import make_password
from django.http import HttpRequest
import json
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import User


@api_view(["GET"])
def api_home(request, *args, **kwargs):
    return Response({"message": "I'm Alive!"})


@api_view(["POST"])
def api_register_user(request: HttpRequest, *args, **kwargs):
    payload = json.loads(request.body)

    username_exists = User.objects.filter(username=payload['username']).exists()
    email_exists = User.objects.filter(email=payload['email']).exists()

    if not (username_exists or email_exists):
        hashed_password = make_password(payload['password'])
        new_user = User.objects.create(
            username=payload['username'],
            password=hashed_password,
            email=payload['email'],
            subscription_status='free'
        )

        DjangoUser.objects.create_user(username=payload['username'], email=payload['email'], password=hashed_password)
        return Response(status=201)
    else:
        return Response({"message": "Username or email already exists!"}, status=400)


@api_view(["POST"])
def api_login_user(request: HttpRequest, *args, **kwargs):
    payload = json.loads(request.body)
    username = payload.get('username')
    password = payload.get('password')

    user = authenticate(request, username=username, password=password)

    if user is not None:
        login(request, user)
        return Response({"message": "Login successful!"}, status=200)
    else:
        return Response({"message": "Invalid credentials"}, status=401)

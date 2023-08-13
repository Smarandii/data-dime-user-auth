from rest_framework import serializers
from .models import User


class UserRegistrationSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=30)
    password = serializers.CharField(write_only=True)  # Ensure password is write-only
    email = serializers.EmailField()
    subscription_status = serializers.ChoiceField(choices=['free', 'paid'], default='free')

    def create(self, validated_data):
        return User.objects.create(**validated_data)


class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=30)
    password = serializers.CharField(write_only=True)

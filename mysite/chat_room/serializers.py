from rest_framework import serializers
from chat_room.models import Room, Chat
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    """Сериализация пользователя"""
    class Meta:
        model = User
        fields = ("id", "username")

class RoomSerializer(serializers.ModelSerializer):
    """Сериализация комнат чата"""
    creator = UserSerializer()
    invited_users = UserSerializer(many=True)
    class Meta:
        model = Room
        fields = ('creator', 'invited_users', 'date')

class ChatSerializer(serializers.ModelSerializer):
    """Сериализация чата"""
    class Meta:
        model = Chat
        fields = ('room', 'user', 'text', 'date')
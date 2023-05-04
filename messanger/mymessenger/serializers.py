from rest_framework import serializers
from .models import MessangerUser, Message, Chat


class MessangerUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = MessangerUser
        fields = ('nickname', 'email', 'image')


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ('messageAuthor', 'text', 'to')


class ChatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chat
        fields = ('title', 'members', 'messages')
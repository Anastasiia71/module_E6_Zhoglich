from django import forms
from .models import MessangerUser, Message, Chat


class MessangerUserForm(forms.ModelForm):
    class Meta:
        model = MessangerUser
        fields = [
            'nickname',
        ]


class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = [
            'messageAuthor',
            'text',
            'to',
        ]


class ChatForm(forms.ModelForm):
    class Meta:
        model = Chat
        fields = [
            'title',
            'members',
            'messages',
        ]
from django.shortcuts import render
from .models import MessangerUser, Message, Chat
from .forms import MessangerUserForm, MessageForm, ChatForm
from .serializers import MessangerUserSerializer, MessageSerializer, ChatSerializer
from rest_framework import generics
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView


class MessangerUserListCreate(generics.ListCreateAPIView):
    queryset = MessangerUser.objects.all()
    serializer_class = MessangerUserSerializer


class MessangerUserList(ListView):
    model = MessangerUser
    ordering = 'nickname'
    template_name = 'MessangerUsers.html'
    context_object_name = 'MessangerUsers'


class MessangerUserDetail(DetailView):
    model = MessangerUser
    template_name = 'MessangerUser.html'
    context_object_name = 'MessangerUser'


class MessangerUserUpdate(UpdateView):
    form_class = MessangerUserForm
    model = MessangerUser
    template_name = 'MessangerUser_update.html'


class MessageListCreate(generics.ListCreateAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer


class MessageList(ListView):
    model = Message
    ordering = 'messageAuthor'
    template_name = 'Messages.html'
    context_object_name = 'Messages'


class MessageDetail(DetailView):
    model = Message
    template_name = 'Message.html'
    context_object_name = 'Message'


class MessageCreate(CreateView):
    form_class = MessageForm
    model = Message
    template_name = 'Message_create.html'


class ChatListCreate(generics.ListCreateAPIView):
    queryset = Chat.objects.all()
    serializer_class = ChatSerializer


class ChatList(ListView):
    model = Chat
    ordering = 'title'
    template_name = 'Chats.html'
    context_object_name = 'Chats'


class ChatDetail(DetailView):
    model = Chat
    template_name = 'Chat.html'
    context_object_name = 'Chat'


class ChatCreate(CreateView):
    form_class = ChatForm
    model = Chat
    template_name = 'Chat_create.html'

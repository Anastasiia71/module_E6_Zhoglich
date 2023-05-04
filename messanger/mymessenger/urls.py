from django.urls import path
from . import views

urlpatterns = [
    path('api/user/', views.MessangerUserListCreate.as_view()),
    path('api/message/', views.MessageListCreate.as_view()),
    path('api/chat/', views.ChatListCreate.as_view()),

    path('', views.MessangerUserList.as_view(), name='MessangerUser_list'),
    path('<int:pk>', views.MessangerUserDetail.as_view(), name='MessangerUser_detail'),
    path('<int:pk>/edit/', views.MessangerUserUpdate.as_view(), name='MessangerUser_update'),
    path('message/', views.MessageList.as_view(), name='Message_list'),
    path('message/<int:pk>', views.MessageDetail.as_view(), name='Message_detail'),
    path('message/create/', views.MessageCreate.as_view(), name='Message_create'),
    path('chat/', views.ChatList.as_view(), name='Chat_list'),
    path('chat/<int:pk>', views.ChatDetail.as_view(), name='Chat_detail'),
    path('chat/create/', views.ChatCreate.as_view(), name='Chat_create'),
]
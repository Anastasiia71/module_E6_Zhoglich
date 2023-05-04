from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class MessangerUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nickname = models.CharField(max_length=15)
    email = models.EmailField
    image = models.ImageField

    def __str__(self):
        return f'{self.image} : {self.nickname}'

    # def get_absolute_url(self):
    #     return reverse('MessangerUser_id', args=[str(self.id)])


class Message(models.Model):
    messageAuthor = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    to = models.OneToOneField(MessangerUser, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.messageAuthor} : {self.text}'

    # def get_absolute_url(self):
    #     return reverse('Message_detail', args=[str(self.id)])


class Chat(models.Model):
    title = models.CharField(max_length=128)
    members = models.ForeignKey(MessangerUser, on_delete=models.CASCADE)
    messages = models.ForeignKey(Message, on_delete=models.CASCADE)

    # def get_absolute_url(self):
    #     return reverse('Chat_detail', args=[str(self.id)])


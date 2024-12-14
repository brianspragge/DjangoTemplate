from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Server(models.Model):
    name = models.CharField(max_length=100)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='owned_servers')
    members = models.ManyToManyField(User, related_name='servers')

    def __str__(self):
        return self.name


class Channel(models.Model):
    server = models.ForeignKey(Server, on_delete=models.CASCADE, related_name='channels')
    name = models.CharField(max_length=100)
    is_voice = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.server.name} - {self.name}"


class Message(models.Model):
    channel = models.ForeignKey(Channel, on_delete=models.CASCADE, related_name='messages')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='channel_messages')
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.author.address}: {self.content[:50]}..."

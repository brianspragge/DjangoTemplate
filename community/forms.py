from django import forms
from .models import Server, Channel, Message

class ServerForm(forms.ModelForm):
    class Meta:
        model = Server
        fields = ['name']

class ChannelForm(forms.ModelForm):
    class Meta:
        model = Channel
        fields = ['name', 'is_voice']

class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['content']

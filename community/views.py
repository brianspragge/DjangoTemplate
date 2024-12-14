from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from .models import Server, Channel, Message
from .forms import ServerForm, ChannelForm, MessageForm

User = get_user_model()

@login_required
def create_server(request):
    if request.method == 'POST':
        form = ServerForm(request.POST)
        if form.is_valid():
            server = form.save(commit=False)
            server.owner = request.user
            server.save()
            server.members.add(request.user)
            return redirect('community:server_list')
    else:
        form = ServerForm()
    return render(request, 'community/create_server.html', {'form': form})

@login_required
def server_list(request):
    servers = Server.objects.filter(members=request.user)
    return render(request, 'community/server_list.html', {'servers': servers})

@login_required
def server_channels(request, server_id):
    server = Server.objects.get(id=server_id)
    if request.method == 'POST':
        form = ChannelForm(request.POST)
        if form.is_valid():
            channel = form.save(commit=False)
            channel.server = server
            channel.save()
            return redirect('community:server_channels', server_id=server_id)
    else:
        form = ChannelForm()

    channels = Channel.objects.filter(server=server)
    return render(request, 'community/server_channels.html', {'server': server, 'channels': channels, 'form': form})

@login_required
def channel_chat(request, channel_id):
    channel = Channel.objects.get(id=channel_id)
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.channel = channel
            message.author = request.user
            message.save()
            return redirect('community:channel_chat', channel_id=channel_id)
    else:
        form = MessageForm()

    messages = Message.objects.filter(channel=channel).order_by('timestamp')
    return render(request, 'community/channel_chat.html', {'channel': channel, 'messages': messages, 'form': form})

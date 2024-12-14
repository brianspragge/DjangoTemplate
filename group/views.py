from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.contrib.auth import get_user_model
from .models import Group, Message
from .forms import GroupForm, MessageForm

User = get_user_model()

@login_required
def create_group(request):
    if request.method == 'POST':
        form = GroupForm(request.POST)
        if form.is_valid():
            group = form.save(commit=False)
            group.created_by = request.user
            group.save()
            group.members.add(request.user)  # Add creator as member
            return redirect(reverse('group:group_list'))
    else:
        form = GroupForm()
    return render(request, 'group/create_group.html', {'form': form})

@login_required
def group_list(request):
    groups = Group.objects.filter(members=request.user)
    return render(request, 'group/group_list.html', {'groups': groups})

@login_required
def group_chat(request, group_id):
    group = Group.objects.get(id=group_id)
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.group = group
            message.sender = request.user
            message.save()
            return redirect(reverse('group:group_chat', kwargs={'group_id':group_id}))
    else:
        form = MessageForm()

    messages = Message.objects.filter(group=group).order_by('timestamp')
    return render(request, 'group/group_chat.html', {'group': group, 'messages': messages, 'form': form})

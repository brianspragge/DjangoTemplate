from django.db.models import Q
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from mail.models import Email
from group.models import Group, Message as GroupMessage
from community.models import Server
from social.models import Post
from message.models import Conversation, Message as ConversationMessage

def search(request):
    query = request.GET.get('q')
    if query:
        emails = Email.objects.filter(Q(subject__icontains=query) | Q(body__icontains=query))
        groups = Group.objects.filter(name__icontains=query)
        servers = Server.objects.filter(name__icontains=query)
        posts = Post.objects.filter(content__icontains=query)
        group_messages = GroupMessage.objects.filter(content__icontains=query)
        conversation_messages = ConversationMessage.objects.filter(content__icontains=query)

        results = {
            'emails': emails,
            'groups': groups,
            'servers': servers,
            'posts': posts,
            'group_messages': group_messages,
            'conversation_messages': conversation_messages,
        }
    else:
        results = {}

    return render(request, 'search.html', {'query': query, 'results': results})

@login_required
def dashboard(request):
    user = request.user
    context = {
        'emails': Email.objects.filter(recipient=user)[:5],
        'groups': Group.objects.filter(members=user)[:3],
        'servers': Server.objects.filter(members=user)[:3],
        'posts': Post.objects.filter(author=user)[:5],
        'conversations': Conversation.objects.filter(participants=user)[:3],
    }
    for conversation in context['conversations']:
        conversation.other_participants = conversation.participants.exclude(address=user.address)

    return render(request, 'dashboard.html', context)

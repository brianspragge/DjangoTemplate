from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from .models import Conversation, Message
from .forms import MessageForm

@login_required
def conversations_list(request):
    conversations = Conversation.objects.filter(participants=request.user)

    for conversation in conversations:
        other_participants = conversation.participants.exclude(address=request.user.address)
        if other_participants.exists():
            conversation.other_participant_address = other_participants.first().address
        else:
            conversation.other_participant_address = None

    return render(request, 'message/conversations_list.html', {'conversations': conversations})

@login_required
def conversation_detail(request, conversation_id):
    conversation = get_object_or_404(Conversation, id=conversation_id)
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.conversation = conversation
            message.sender = request.user
            message.save()
            return redirect(reverse('message:conversation_detail', kwargs={'conversation_id':conversation_id}))
    else:
        form = MessageForm()

    messages = Message.objects.filter(conversation=conversation).order_by('timestamp')
    return render(request, 'message/conversation_detail.html', {'conversation': conversation, 'messages': messages, 'form': form})

@login_required
def new_conversation(request):
    if request.method == 'POST':
        # Assuming form data includes 'recipient_address'
        recipient_address = request.POST.get('recipient_address')
        try:
            recipient = User.objects.get(address=recipient_address)
            conversation = Conversation.objects.create()
            conversation.participants.add(request.user, recipient)
            return redirect(reverse('message:conversation_detail', kwargs={'conversation_id':conversation.id}))
        except User.DoesNotExist:
            # Handle case where user does not exist
            return render(request, 'message/new_conversation.html', {'error': 'User does not exist'})
    return render(request, 'message/new_conversation.html')

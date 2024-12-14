from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.contrib.auth import get_user_model
from .models import Email
from .forms import EmailForm

User = get_user_model()

@login_required
def send_email(request):
    if request.method == 'POST':
        form = EmailForm(request.POST)
        if form.is_valid():
            email = form.save(commit=False)
            email.sender = request.user
            email.save()
            return redirect(reverse('mail:inbox'))
    else:
        form = EmailForm()
    return render(request, 'mail/send_email.html', {'form': form})

@login_required
def inbox(request):
    emails = Email.objects.filter(recipient=request.user)
    return render(request, 'mail/inbox.html', {'emails': emails})

from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.urls import reverse
from .forms import CustomAuthenticationForm, CustomUserCreationForm

def login_view(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect(request.GET.get('next', reverse('home:dashboard')))
    else:
        form = CustomAuthenticationForm()
    return render(request, 'user_auth/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect(reverse('user_auth:login'))

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user, backend='user_auth.backends.AddressBackend')
            return redirect(reverse('home:dashboard'))
    else:
        form = CustomUserCreationForm()
    return render(request, 'user_auth/register.html', {'form': form})

from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .models import User

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('address', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)
        self.fields['address'].widget.attrs.update({'placeholder': 'Enter your address'})
        self.fields['password1'].widget.attrs.update({'placeholder': 'Enter your password'})
        self.fields['password2'].widget.attrs.update({'placeholder': 'Confirm your password'})


class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(label="Address")  # Renaming 'username' to 'Address' to match your user model

    # Customizing field display
    def __init__(self, *args, **kwargs):
        super(CustomAuthenticationForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'placeholder': 'Enter your address'})
        self.fields['password'].widget.attrs.update({'placeholder': 'Enter your password'})

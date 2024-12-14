from django import forms
from .models import Email

class EmailForm(forms.ModelForm):
    class Meta:
        model = Email
        fields = ['recipient', 'subject', 'body']

    recipient = forms.CharField()

    def clean_recipient(self):
        recipient_address = self.cleaned_data['recipient']
        try:
            user = User.objects.get(address=recipient_address)
            return user
        except User.DoesNotExist:
            raise forms.ValidationError("Recipient does not exist.")

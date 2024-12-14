from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone

User = get_user_model()

class Email(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_emails')
    recipient = models.ForeignKey(User, on_delete=models.CASCADE, related_name='received_emails')
    subject = models.CharField(max_length=255)
    body = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    forwarded_from = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, related_name='forwarded_emails')

    def __str__(self):
        return f"{self.subject} to {self.recipient.address}"

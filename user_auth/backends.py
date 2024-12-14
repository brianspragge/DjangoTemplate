from django.contrib.auth.backends import ModelBackend
from .models import User


class AddressBackend(ModelBackend):
    def authenticate(self, request, address=None, password=None, **kwargs):
        try:
            user = User.objects.get(address=address)
            if user.check_password(password):
                return user
        except User.DoesNotExist:
            return None

from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin


class UserManager(BaseUserManager):
    def create_user(self, address, password=None):
        if not address:
            raise ValueError('Users must have a unique address')
        user = self.model(address=address)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, address, password):
        user = self.create_user(address, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    address = models.CharField(max_length=255, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'address'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.address

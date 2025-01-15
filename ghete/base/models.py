from django.db import models
from django.contrib.auth.models import AbstractUser,BaseUserManager



class CustomUserManager(BaseUserManager):
    def create_user(self, phone_number, password=None):
        if not phone_number:
            raise ValueError('Users must have a valid phone number')

        user = self.model(phone_number=phone_number)
        user.set_password(password)
        user.save(using=self._db)
        return user
    def create_superuser(self, phone_number, password):
        user = self.create_user(phone_number, password)
        user.is_admin = True
        user.save(using=self._db)
        return user

class CustomUser(AbstractUser):
    phone_number = models.CharField(max_length=11, unique=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = CustomUserManager()
    USERNAME_FIELD = 'phone_number'

    REQUIRED_FIELDS = []
    def __str__(self):
        return self.phone_number
    def has_perms(self, perm, obj = None):
        return True
    def has_module_perms(self, app_label):
        return True


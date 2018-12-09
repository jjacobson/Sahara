# users/models.py
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _
from django.db import models


class CustomUser(AbstractUser):
    email = models.EmailField(_("email"), max_length=255, unique=True)
    first_name = models.CharField(_("first_name"), max_length=30)
    last_name = models.CharField(_("last_name"), max_length=30)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'username']

    def __str__(self):
        return self.email

    def get_full_name(self):
        return self.first_name + ' ' + self.last_name

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _


class CustomUser(AbstractUser):
    email = models.EmailField(_('email address'), unique=True)
    username = models.CharField(max_length=255, unique=False, blank=True, null=True)

    def __str__(self):
        return self.email

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _


class CustomUser(AbstractUser):
    # add additional fields in here
    email = models.EmailField(_('Email address'), unique=True)

    def __str__(self):
        return self.username

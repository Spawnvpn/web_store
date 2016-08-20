from django.contrib.auth.models import AbstractUser
from django.db import models


class WebStoreUser(AbstractUser):
    birth_date = models.DateField()
    phone_number = models.CharField(max_length=16)

    def __str__(self):
        return self.username

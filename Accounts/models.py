from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    Gender_choices = [
        ("M","Male"),
         ("F","Female")
    ]
    gender = models.CharField(max_length=1, choices=Gender_choices)


# Create your models here.

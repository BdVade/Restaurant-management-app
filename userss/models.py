from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
import uuid

# Create your models here.
CHOICES = [('Manager','Manager'),('Counter','Counter'),('Kitchen','Kitchen'),('Ordinary','Ordinary')]


class User(AbstractUser):
    type = models.CharField(choices=CHOICES,default='Ordinary',max_length=10)




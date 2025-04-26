from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class User(models.Model):
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=15)
    password = models.CharField(max_length=128)
    confirm_password = models.CharField(max_length=128)
    image = models.ImageField(upload_to='profile_images/', null=True, blank=True)

    def __str__(self):
        return self.email


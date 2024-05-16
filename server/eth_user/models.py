from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    public_key = models.CharField(max_length=64, unique=True, blank=True, null=True)
    profile_image = models.ImageField(upload_to="user/image/", blank=True, null=True)
    username = models.CharField(max_length=32, unique=True, blank=True, null=True)
    password = models.CharField(max_length=128, blank=True, null=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.username if self.username is not None else "username " + str(self.id)

class Captcha(models.Model):
    captcha = models.CharField(max_length=46)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.captcha[:8] + '...'


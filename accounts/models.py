from django.db import models
from django.contrib.auth.models import User


class ProfileUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    favorite_book = models.CharField(max_length=100, blank=True, null=True)
    location = models.CharField(max_length=100, blank=True, null=True)
    profile_picture = models.ImageField(blank=True, null=True, upload_to='profiles')

    def __str__(self):
        return f'{self.user}'

from django.db import models
from django.contrib.auth.models import User


class ProfileUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.URLField(default='https://www.pngitem.com/pimgs/m/146-1468843_profile-icon-orange-png-transparent-png.png')
    favorite_book = models.CharField(max_length=60, blank=True, null=True)
    location = models.CharField(max_length=60, blank=True, null=True)

    def __str__(self):
        return f'{self.user}'

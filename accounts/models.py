from django.db import models
from django.contrib.auth.models import User


class ProfileUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.URLField(default='https://image.flaticon.com/icons/png/128/3135/3135715.png')

    def __str__(self):
        return f'{self.user}'

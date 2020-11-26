from django.db import models

from accounts.models import ProfileUser


class Quote(models.Model):
    user = models.ForeignKey(ProfileUser, on_delete=models.CASCADE)
    text = models.CharField(max_length=255)
    author = models.CharField(max_length=80)
    image_url = models.URLField(blank=True, null=True)

    def __str__(self):
        return f'{self.author} said "{self.text[:20]}...'


class Like(models.Model):
    quote = models.ForeignKey(Quote, on_delete=models.CASCADE)
    test = models.CharField(max_length=2, null=True)

from django.conf import settings
from django.db import models

from django.contrib.auth.models import User

class SecrectFriend(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="me")
    secret_friend = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True, related_name='secret_friend')

    def __str__(self):
        return self.user.username

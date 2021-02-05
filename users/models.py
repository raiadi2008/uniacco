from django.db import models
from rest_framework_simplejwt.tokens import RefreshToken

class User(models.Model):
    username = models.CharField(max_length=65, blank=False, unique=True)
    password = models.CharField(max_length=200, blank=False)

    def __str__(self):
        return self.username

    def token(self):
        refresh=RefreshToken.for_user(self)
        return {
            'refresh':str(refresh),
            'access':str(refresh.access_token)
        }
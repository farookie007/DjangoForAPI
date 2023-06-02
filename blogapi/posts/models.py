from django.db import models
from django.conf import settings# [alternatively]from django.contrib.auth import get_user_model


class Post(models.Model):
    title = models.CharField(max_length=50)
    body = models.TextField()
    # [alternatively]author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

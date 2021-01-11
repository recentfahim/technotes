from django.db import models
from django.contrib.auth import get_user_model


class Note(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)

    USERNAME_FIELD = 'email'

    def __str__(self):
        return self.title

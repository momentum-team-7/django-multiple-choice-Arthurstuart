from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    pass

class Snippet(models.Model):
    title = models.CharField(max_length=60)
    language = models.CharField(max_length=20)
    description = models.CharField(max_length=300)
    script = models.TextField(max_length=1000)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.title


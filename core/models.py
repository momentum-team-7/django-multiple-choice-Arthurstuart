from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models import Count

Languages = (
    ('HTML', 'HTML'),
    ('CSS', 'CSS'),
    ('JavaScript', 'JavaScript'),
    ('Python', 'Python'),
    ('Django', 'Django')
)

class User(AbstractUser):
    pass

class Snippet(models.Model):
    title = models.CharField(max_length=60)
    language = models.CharField(max_length=20, choices=Languages)
    description = models.CharField(max_length=300)
    script = models.TextField(max_length=1000)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name='snippets_owned')
    author = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name='snippets_authored')
    tags = models.ManyToManyField('Tag', blank=True)

    def __str__(self):
        return self.title

class Tag(models.Model):
    tag = models.CharField(max_length=60, unique=True)
    language = models.CharField(max_length=20, choices=Languages)

    def __str__(self):
        return self.tag
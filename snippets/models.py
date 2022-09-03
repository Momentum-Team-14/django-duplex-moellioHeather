from django.db import models
from django.contrib.auth.models import AbstractUser as BaseUser
from django.urls import reverse
from django.db.models import Q


# Create your models here.
class User(BaseUser):
    pass


class SnippetManager(models.Manager):
    def search(self, query):
        lookups = lookups = Q(title__icontains=query) | Q(description__icontains=query) | Q(
            code__icontains=query) | Q(language__icontains=query)
        return self.get_queryset().filter(lookups)


class Snippet(models.Model):
    title = models.CharField(max_length=100)
    code = models.TextField()
    description = models.CharField(max_length=512, default="")
    project = models.CharField(max_length=100, blank=True, null=True)
    language = models.ForeignKey(
        'Language', on_delete=models.CASCADE, related_name="snippets", blank=True, null=True)
    # related name should be the plural of the model that it's in. This is a O2M relationship. A snippet has one user. A user has many snippets.
    # if I want to have more than one user associated with a snippet, I use an M2M field
    users = models.ManyToManyField('User', related_name='snippets')
    author = models.ForeignKey(
        'User', on_delete=models.CASCADE, related_name="my_snippets")
    parent = models.ForeignKey(
        'Snippet', on_delete=models.SET_NULL, related_name='forks', blank=True, null=True)

    @property
    def get_project(self):
        if self.project:
            return self.project
        else:
            return "N/A"

    def __str__(self):
        return f'{self.title}'


class Language(models.Model):
    name = models.CharField(max_length=255)
    version = models.FloatField(blank=True, null=True)

    def __str__(self):
        return f'{self.name}'

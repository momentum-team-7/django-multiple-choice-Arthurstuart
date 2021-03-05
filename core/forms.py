from django import forms
from .models import Snippet


class SnippetForm(forms.SnippetForm):
    class Meta:
        model = Snippet
        fields = ['title', 'language', 'description', 'script', 'user']
from django.forms import ModelForm
from .models import Snippet, Language


class SnippetForm(ModelForm):
    # creates form from the model Snippet
    class Meta:
        model = Snippet
        fields = ['title', 'code', 'description', 'project', 'language']

from django import forms
from django.forms import ModelForm
from .models import NewsStory, Comment
from django.utils import timezone

choices = [('coding', 'coding'), ('social', 'social'), ('life-hacks', 'life-hacks'), ('events', 'events')]
class StoryForm(ModelForm):
    class Meta:
        model = NewsStory
        fields = ["title", "pub_date", "content"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['pub_date'].initial = timezone.now().strftime("%Y-%m-%dT%H:%M")


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ["name", "body"]
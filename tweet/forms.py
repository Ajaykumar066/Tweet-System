from django import forms
from .models import tweet

class tweetForm(forms.ModelForm):
    class Meta:
        model = tweet
        fields = ['text','photo']
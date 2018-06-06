from django import forms
from .models import Post
from django.forms import ModelForm


class HomeForm(forms.ModelForm):
    Player = forms.CharField()

    class Meta:
        model = Post
        fields = ()


class LetterForm(forms.Form):
    Letter = forms.CharField()

    class Meta:
        fields = ('Letter',)

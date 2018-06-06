from django.apps import AppConfig
from .models import Post
from .forms import HomeForm, LetterForm


class HangmanConfig(AppConfig):
    name = 'hangman'

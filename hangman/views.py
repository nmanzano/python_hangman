from django.shortcuts import render
from .models import Post
from django.shortcuts import render, get_object_or_404, redirect
from .forms import HomeForm, LetterForm
from .apps import HangmanConfig
from .utility import Game


def home_view(request):
    formPlayer = HomeForm(request.POST)
    gameView = False
    posts = Post.objects.all()
    args = {
        'posts': posts,
        'form': formPlayer,
        'gameView': gameView
            }
    return render(request, 'hangman/base.html', args)


def game_view(request):
    posts = Post.objects.all()
    letterForm = LetterForm(request.POST)
    gameView = True

    if request.method == 'POST':
        formPlayer = HomeForm(request.POST)
        if formPlayer.is_valid():
            game = Game()
            post = formPlayer.save(commit=False)
            post.player = request.POST.get('Player', '')
            post.wordsofar = game.setup_dashes()
            print(len(post.wordsofar), 'line 33')
            post.lives = game.lives_setup()
            post.save()

    args = {
        'letterForm': letterForm,
        'gameView': gameView,
        'posts': posts
    }
    return render(request, 'hangman/word.html', args)


def letter_submission(request):
    posts = Post.objects.all()
    for post in posts:
        lives = post.lives

    game = Game()
    letter = request.POST.get('Letter', '')
    choice = game.choose(letter)
    return redirect('game_view')

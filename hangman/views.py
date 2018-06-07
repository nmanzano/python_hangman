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
            post.lives = game.lives_setup()
            post.word = game.setword()
            post.masterword = list(post.word)
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
        correct = (post.correct)
        wordsofar = list(post.wordsofar)
        masterword = post.masterword

    game = Game()
    letter = request.POST.get('Letter', '')
    choice = game.choose(letter)

    checkposts = Post.objects.all()
    for checkpost in checkposts:
        checksifwon = checkpost.wordsofar
        checkiflost = checkpost.lives

    if checksifwon == 'WINNER!':
        Post.objects.all()[0].delete()
        return redirect('https://youtu.be/oHg5SJYRHA0?t=44')
    elif checkiflost == 0:
        Post.objects.all()[0].delete()
        return redirect('https://youtu.be/nlYlNF30bVg?t=13')

    return redirect('game_view')


def won():
    Post.objects.all()[0].delete()
    return "WINNER!"


def lost():
    pass

from .models import Post
from .forms import HomeForm, LetterForm
from . import views


class Game(object):

    def __init__(self):
        self.word = 'longhorns'
        self.wordsofar = []
        self.masterword = list(self.word)
        self.choice = ''

    def setup_dashes(self):
        for letter in self.masterword:
            self.wordsofar.append('_')
        self.wordsofar = ''.join(self.wordsofar)
        return self.wordsofar.replace(' ', '')

    def setword(self):
        return self.word

    def lives_setup(self):
        return len(self.masterword)

    def choose(self, choice):
        self.choice = choice
        if self.choice in self.wordsofar:
            return self.incorrect(self.choice)
        elif self.choice in self.masterword:
            return self.correct(self.choice)
        else:
            return self.incorrect(self.choice)

    def incorrect(self, choice):
        posts = Post.objects.all()
        for post in posts:
            lives = post.lives
            incorrect = post.incorrect

        lives -= 1

        post.lives = lives
        post.incorrect = incorrect + ' ' + choice
        post.save()
        return(choice)

    def correct(self, choice):
        posts = Post.objects.all()
        for post in posts:
            correct = post.correct
            wordsofar = post.wordsofar
            masterword = post.masterword

        checkmark = self.fill_in_blanks(choice)
        print(checkmark, 'line 64')
        post.wordsofar = checkmark
        post.correct = correct + ' ' + choice
        post.save()

        return(checkmark)

    def fill_in_blanks(self, choice):
        posts = Post.objects.all()
        for post in posts:
            # print (post.__dict__)
            wordsofar = post.wordsofar
        wordsofar = list(wordsofar)
        letter = [index for index, value in enumerate(self.masterword)
                  if value == choice]
        for index in letter:
            wordsofar[index] = self.masterword[index]
        if self.masterword == wordsofar:
            return views.won()
        return ''.join(wordsofar)

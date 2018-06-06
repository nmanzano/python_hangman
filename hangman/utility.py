from .models import Post
from .forms import HomeForm, LetterForm


class Game(object):

    def __init__(self):
        self.word = 'longhorns'
        self.wordsofar = []
        self.masterword = list(self.word)
        self.choice = ''

    def setup_dashes(self):
        for letter in self.masterword:
            self.wordsofar.append(' _ ')

        return self.wordsofar

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

        lives = lives - 1

        args = {
            'lives': lives,
            'choice': choice,
            'incorrect': incorrect
        }
        post.lives = lives
        post.incorrect = incorrect + ' ' + choice
        post.save()
        return(args)

    def correct(self, choice):
        posts = Post.objects.all()
        # cheese = posts.get('wordsofar', '')
        # print(cheese, 'line 51')
        print(type(posts), 'line 53')
        print(Post.wordsofar, 'line 54')
        for post in posts:
            print(post.wordsofar, 'Line 56')
            correct = post.correct
            wordsofar = post.wordsofar
            print(wordsofar, 'Line 59')
        print(type(wordsofar), 'line 60')
        print(len(list(wordsofar)), 'Line 61')

        checkmark = self.fill_in_blanks(choice)
        print(checkmark, 'line 64')
        args = {
            'choice': choice,
        }
        post.correct = correct + ' ' + choice
        post.save()
        return(args)
        # if wordsofar == self.masterword:
        #     print ('You Won!')
        # else:
        #     startgame()

    def fill_in_blanks(self, choice):
        posts = Post.objects.all()
        for post in posts:
            wordsofar = post.wordsofar
        print(wordsofar, 'line 80')
        print(len(wordsofar), 'line 81')
        # letter = [index for index, value in enumerate(self.masterword) if value == choice]
        # for index in letter:
        #     wordsofar[index] = self.masterword[index]
        return wordsofar

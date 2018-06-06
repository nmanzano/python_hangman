from django.db import models
from django.utils import timezone


class Post(models.Model):
    player = models.CharField(max_length=500)
    incorrect = models.CharField(max_length=500)
    correct = models.CharField(max_length=500)
    lives = models.PositiveSmallIntegerField(default=0)
    wordsofar = models.CharField(max_length=500, default='STRING')
    nameLength = models.PositiveSmallIntegerField(default=0)
    word = models.CharField(max_length=500, default='STRING')
    letter = models.CharField(max_length=500, default='STRING')

    def __str__(self):
        return self.player
        return self.incorrect
        return self.correct
        return self.lives
        return self.wordsofar
        return self.nameLength
        return self.word
        return self.letter
        return self.word_length

from django.db import models
from django.utils import timezone


class Post(models.Model):
    player = models.CharField(max_length=500)
    incorrect = models.CharField(max_length=500)
    correct = models.CharField(max_length=500)
    lives = models.PositiveSmallIntegerField(default=0)
    wordsofar = models.CharField(max_length=500, default='STRING')
    masterword = models.CharField(max_length=500, default='STRING')
    word = models.CharField(max_length=500, default='STRING')
    letter = models.CharField(max_length=500, default='STRING')

    def __str__(self):
        return self.player

    def seperate_lines(self):
        return ' '.join(self.wordsofar)

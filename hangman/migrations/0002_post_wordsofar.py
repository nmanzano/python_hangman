# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-05-31 14:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hangman', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='wordsofar',
            field=models.CharField(default='STRING', max_length=500),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-06-05 04:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hangman', '0005_post_letter'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='word_length',
            field=models.PositiveSmallIntegerField(default=0),
        ),
    ]

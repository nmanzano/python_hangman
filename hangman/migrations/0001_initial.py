# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-05-30 20:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('player', models.CharField(max_length=500)),
                ('incorrect', models.CharField(max_length=500)),
                ('correct', models.CharField(max_length=500)),
                ('lives', models.PositiveSmallIntegerField(default=0)),
            ],
        ),
    ]

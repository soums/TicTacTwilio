# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('player_1', models.CharField(max_length=30)),
                ('player_2', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Move',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('location', models.IntegerField(default=0)),
                ('marker', models.CharField(max_length=1)),
                ('game_id', models.ForeignKey(to='games.Game')),
            ],
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0016_auto_20150817_1656'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='scoredUsers',
            field=models.ManyToManyField(to='polls.UserProfile', null=True),
        ),
        migrations.AlterField(
            model_name='comment',
            name='numberOfLikes',
            field=models.IntegerField(default=0),
        ),
    ]

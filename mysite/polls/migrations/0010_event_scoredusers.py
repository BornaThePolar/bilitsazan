# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0009_remove_event_scoredusers'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='scoredUsers',
            field=models.ForeignKey(to='polls.Scorers', null=True),
        ),
    ]

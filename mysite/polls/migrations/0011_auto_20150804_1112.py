# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0010_event_scoredusers'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='scoredUsers',
        ),
        migrations.RemoveField(
            model_name='event',
            name='user',
        ),
    ]

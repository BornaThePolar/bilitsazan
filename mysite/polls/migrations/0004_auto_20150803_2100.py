# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_event_ticketssold'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='photo',
            field=models.FileField(upload_to=b'event_photoes/'),
        ),
        migrations.AlterField(
            model_name='event',
            name='score',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='event',
            name='scoredUsers',
            field=models.ForeignKey(to='polls.Scorers', null=True),
        ),
    ]

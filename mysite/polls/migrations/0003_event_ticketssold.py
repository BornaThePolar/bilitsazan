# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_auto_20150727_1716'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='ticketsSold',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0004_auto_20150803_2100'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='photo',
            field=models.FileField(upload_to='event_photoes/'),
        ),
        migrations.AlterField(
            model_name='event',
            name='ticketsSold',
            field=models.IntegerField(default=0),
        ),
    ]

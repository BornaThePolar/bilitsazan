# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0014_auto_20150816_2157'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='numberofScorers',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='event',
            name='score',
            field=models.FloatField(default=0),
        ),
    ]

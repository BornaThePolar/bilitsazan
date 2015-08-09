# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0006_auto_20150804_0829'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='score',
            field=models.FloatField(default=3),
        ),
    ]

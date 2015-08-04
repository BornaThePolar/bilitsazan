# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0005_auto_20150803_2104'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='photo',
            field=models.FileField(upload_to='event_photoes/'),
        ),
    ]

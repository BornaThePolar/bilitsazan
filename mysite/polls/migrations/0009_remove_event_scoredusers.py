# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0008_auto_20150804_1059'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='scoredUsers',
        ),
    ]

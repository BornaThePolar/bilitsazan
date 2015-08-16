# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0012_merge'),
    ]

    operations = [
        migrations.CreateModel(
            name='EventTicketType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('price', models.IntegerField()),
                ('tickets', models.IntegerField()),
            ],
        ),
        migrations.RemoveField(
            model_name='event',
            name='price',
        ),
        migrations.RemoveField(
            model_name='event',
            name='ticketsLeft',
        ),
        migrations.RemoveField(
            model_name='event',
            name='ticketsSold',
        ),
        migrations.AddField(
            model_name='eventtickettype',
            name='event',
            field=models.ForeignKey(to='polls.Event'),
        ),
    ]

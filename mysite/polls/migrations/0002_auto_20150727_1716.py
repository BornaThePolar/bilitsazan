# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Buy',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('rahgiriCode', models.IntegerField()),
                ('price', models.IntegerField()),
                ('date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('content', models.TextField()),
                ('time', models.DateTimeField(default=datetime.datetime.now)),
                ('numberOfLikes', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateField()),
                ('ticketsLeft', models.IntegerField()),
                ('description', models.TextField()),
                ('subject', models.CharField(max_length=32)),
                ('finishDate', models.DateField()),
                ('price', models.IntegerField()),
                ('photo', models.FileField(upload_to='static/Photos/Users/')),
                ('score', models.FloatField()),
                ('category', models.ForeignKey(to='polls.Category')),
            ],
        ),
        migrations.CreateModel(
            name='Likers',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cost', models.IntegerField()),
                ('number', models.IntegerField()),
                ('event', models.ForeignKey(to='polls.Event')),
            ],
        ),
        migrations.CreateModel(
            name='Scorers',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
        ),
        migrations.CreateModel(
            name='SubCategory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=32)),
                ('daste', models.ForeignKey(to='polls.Category')),
            ],
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('type', models.CharField(max_length=32)),
                ('price', models.IntegerField()),
                ('seat', models.IntegerField()),
                ('event', models.ForeignKey(to='polls.Event')),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('gender', models.BooleanField()),
                ('isSuperUSer', models.BooleanField(default=False)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='choice',
            name='question',
        ),
        migrations.DeleteModel(
            name='Choice',
        ),
        migrations.DeleteModel(
            name='Question',
        ),
        migrations.AddField(
            model_name='scorers',
            name='scorers',
            field=models.ManyToManyField(to='polls.UserProfile'),
        ),
        migrations.AddField(
            model_name='order',
            name='user',
            field=models.ForeignKey(to='polls.UserProfile'),
        ),
        migrations.AddField(
            model_name='likers',
            name='user',
            field=models.ManyToManyField(to='polls.UserProfile'),
        ),
        migrations.AddField(
            model_name='event',
            name='scoredUsers',
            field=models.ForeignKey(to='polls.Scorers'),
        ),
        migrations.AddField(
            model_name='event',
            name='subCategory',
            field=models.ForeignKey(to='polls.SubCategory'),
        ),
        migrations.AddField(
            model_name='event',
            name='user',
            field=models.ForeignKey(to='polls.UserProfile'),
        ),
        migrations.AddField(
            model_name='comment',
            name='author',
            field=models.ForeignKey(to='polls.UserProfile'),
        ),
        migrations.AddField(
            model_name='comment',
            name='likes',
            field=models.ForeignKey(to='polls.Likers'),
        ),
    ]

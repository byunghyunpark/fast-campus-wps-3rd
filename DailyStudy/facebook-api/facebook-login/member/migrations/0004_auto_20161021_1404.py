# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-21 14:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0003_auto_20161013_1214'),
    ]

    operations = [
        migrations.AddField(
            model_name='myuser',
            name='facebook_id',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='myuser',
            name='img_profile_url',
            field=models.URLField(blank=True),
        ),
        migrations.AddField(
            model_name='myuser',
            name='is_facebook_user',
            field=models.BooleanField(default=False),
        ),
    ]

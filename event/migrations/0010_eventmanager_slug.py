# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-06 21:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0009_auto_20171106_1540'),
    ]

    operations = [
        migrations.AddField(
            model_name='eventmanager',
            name='slug',
            field=models.SlugField(blank=True, max_length=140, null=True, unique=True),
        ),
    ]

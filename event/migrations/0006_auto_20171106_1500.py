# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-06 20:00
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0005_auto_20171106_1442'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventlocation',
            name='states',
            field=models.CharField(default='North Carolina', max_length=20),
        ),
        migrations.AlterField(
            model_name='eventmanager',
            name='event_end_time',
            field=models.TimeField(default=datetime.time(20, 0, 0, 175757)),
        ),
        migrations.AlterField(
            model_name='eventmanager',
            name='event_start_time',
            field=models.TimeField(default=datetime.time(20, 0, 0, 174757)),
        ),
    ]

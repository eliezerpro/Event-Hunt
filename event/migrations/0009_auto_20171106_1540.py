# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-06 20:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0008_auto_20171106_1508'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventlocation',
            name='states',
            field=models.CharField(default='North Carolina', editable=False, max_length=20),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-08-29 13:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('icf_events', '0009_auto_20190829_1911'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventgallery',
            name='event_slug',
            field=models.CharField(max_length=150),
        ),
    ]

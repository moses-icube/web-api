# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2021-10-07 14:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('icf_career_fair', '0015_auto_20211004_1436'),
    ]

    operations = [
        migrations.AddField(
            model_name='careerfairparticipant',
            name='entity_id',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]

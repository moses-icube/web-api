# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2021-09-29 17:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('icf_career_fair', '0010_auto_20210929_2204'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='participantandproduct',
            name='is_payment_successful',
        ),
        migrations.RemoveField(
            model_name='participantandproduct',
            name='total_cost',
        ),
        migrations.AddField(
            model_name='careerfairparticipant',
            name='is_payment_successful',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='careerfairparticipant',
            name='total_cost',
            field=models.DecimalField(decimal_places=2, max_digits=8, null=True),
        ),
    ]

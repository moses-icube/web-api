# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-01-10 10:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('icf_messages', '0003_icfnotification_deleted_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='icfnotification',
            name='details',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='details'),
        ),
    ]

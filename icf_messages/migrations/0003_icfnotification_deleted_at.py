# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-01-09 04:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('icf_messages', '0002_icfnotification'),
    ]

    operations = [
        migrations.AddField(
            model_name='icfnotification',
            name='deleted_at',
            field=models.DateTimeField(blank=True, null=True, verbose_name='deleted_at'),
        ),
    ]
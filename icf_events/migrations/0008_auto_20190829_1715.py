# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-08-29 11:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('icf_events', '0007_auto_20190829_1433'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='registration_website',
            field=models.URLField(blank=True, null=True),
        ),
    ]
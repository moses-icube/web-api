# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-11-14 09:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('icf_generic', '0002_auto_20181113_1201'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(blank=True, max_length=200),
        ),
    ]

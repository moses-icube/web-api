# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-11-22 09:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('icf_item', '0006_auto_20181121_1914'),
    ]

    operations = [
        migrations.AlterField(
            model_name='itemdraft',
            name='slug',
            field=models.SlugField(blank=True, unique=True),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2020-05-21 08:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('icf_entity', '0007_auto_20200521_1321'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ministrymasterconfig',
            name='industries',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='industries'),
        ),
        migrations.AlterField(
            model_name='ministrymasterconfig',
            name='sectors',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='sectors'),
        ),
    ]

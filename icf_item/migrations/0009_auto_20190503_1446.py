# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-05-03 09:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('icf_item', '0008_auto_20181123_1516'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='description',
            field=models.CharField(max_length=10000, verbose_name='description'),
        ),
        migrations.AlterField(
            model_name='item',
            name='description_en',
            field=models.CharField(max_length=10000, null=True, verbose_name='description'),
        ),
        migrations.AlterField(
            model_name='item',
            name='description_es',
            field=models.CharField(max_length=10000, null=True, verbose_name='description'),
        ),
        migrations.AlterField(
            model_name='item',
            name='description_fr',
            field=models.CharField(max_length=10000, null=True, verbose_name='description'),
        ),
    ]

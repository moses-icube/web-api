# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-07-16 09:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('icf_item', '0009_auto_20190503_1446'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='description',
            field=models.CharField(max_length=30000, verbose_name='description'),
        ),
        migrations.AlterField(
            model_name='item',
            name='description_en',
            field=models.CharField(max_length=30000, null=True, verbose_name='description'),
        ),
        migrations.AlterField(
            model_name='item',
            name='description_es',
            field=models.CharField(max_length=30000, null=True, verbose_name='description'),
        ),
        migrations.AlterField(
            model_name='item',
            name='description_fr',
            field=models.CharField(max_length=30000, null=True, verbose_name='description'),
        ),
    ]
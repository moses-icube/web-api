# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-12-10 09:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('icf_jobs', '0021_userresumecomponent_sort_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usereducation',
            name='certification',
            field=models.CharField(max_length=100, verbose_name='certification'),
        ),
        migrations.AlterField(
            model_name='usereducation',
            name='school',
            field=models.CharField(max_length=100, verbose_name='school'),
        ),
    ]
# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2020-04-24 07:34
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('icf_covid_status', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='currentcompensationstatus',
            options={'ordering': ('name',), 'verbose_name_plural': 'Current Compensation Statuses'},
        ),
        migrations.AlterModelOptions(
            name='currentworkstatus',
            options={'ordering': ('name',), 'verbose_name_plural': 'Current Work Statuses'},
        ),
        migrations.AlterModelOptions(
            name='userworkstatus',
            options={'verbose_name_plural': 'User Work Statuses'},
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2020-10-12 07:21
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('icf_messages', '0005_auto_20201001_1517'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='icfmessage',
            options={'ordering': ['-sent_at', '-id'], 'verbose_name': 'message', 'verbose_name_plural': 'messages'},
        ),
        migrations.AlterModelOptions(
            name='icfnotification',
            options={'ordering': ['-sent_at', '-id'], 'verbose_name': 'notification', 'verbose_name_plural': 'notifications'},
        ),
    ]
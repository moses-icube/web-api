# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-07-18 13:22
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('icf_orders', '0005_auto_20190718_1457'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ActionAndSubscriptionPlan',
            new_name='ActionSubscriptionPlan',
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2021-09-22 15:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('icf_item', '0012_auto_20190730_1158'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='status',
            field=models.SmallIntegerField(choices=[(1, 'Draft'), (2, 'Active'), (3, 'Expired'), (4, 'Closed'), (5, 'Marked for delete'), (6, 'Deleted'), (7, 'Item Under Review'), (8, 'Item Rejected')], default=1),
        ),
        migrations.AlterField(
            model_name='itemdraft',
            name='status',
            field=models.SmallIntegerField(blank=True, choices=[(1, 'Draft'), (2, 'Active'), (3, 'Expired'), (4, 'Closed'), (5, 'Marked for delete'), (6, 'Deleted'), (7, 'Item Under Review'), (8, 'Item Rejected')], null=True),
        ),
    ]
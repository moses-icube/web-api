# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2021-10-23 11:48
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('icf_career_fair', '0019_auto_20211020_1904'),
    ]

    operations = [
        migrations.AlterField(
            model_name='session',
            name='career_fair',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='career_fair_sessions', to='icf_career_fair.CareerFair'),
        ),
        migrations.AlterField(
            model_name='support',
            name='career_fair',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='career_fair_supports', to='icf_career_fair.CareerFair'),
        ),
    ]
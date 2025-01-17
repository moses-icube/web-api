# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2021-10-20 13:34
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('icf_career_fair', '0018_auto_20211020_1903'),
    ]

    operations = [
        migrations.AlterField(
            model_name='speakerandsession',
            name='session',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='speaker_sessions', to='icf_career_fair.Session'),
        ),
        migrations.AlterField(
            model_name='speakerandsession',
            name='speaker',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='speaker_sessions', to='icf_career_fair.Speaker'),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2020-09-03 09:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('icf_jobs', '0025_candidatesearch'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidatesearchforjobmaster',
            name='search_criteria',
            field=models.CharField(choices=[('skill', 'skill'), ('work_experience', 'work_experience'), ('education', 'education'), ('location', 'location')], default='skill', max_length=500, unique=True),
        ),
    ]

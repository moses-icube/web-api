# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2020-06-18 13:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('icf_jobs', '0023_auto_20191218_1610'),
    ]

    operations = [
        migrations.CreateModel(
            name='CandidateSearchForJobMaster',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('search_criteria', models.CharField(choices=[('skill', 'skill'), ('work_experience', 'work_experience'), ('education', 'education'), ('location', 'location')], default='skill', max_length=500)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]

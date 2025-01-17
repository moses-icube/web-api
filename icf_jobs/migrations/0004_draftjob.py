# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-11-19 10:07
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('icf_entity', '0004_auto_20181119_1249'),
        ('icf_jobs', '0003_auto_20181119_1249'),
    ]

    operations = [
        migrations.CreateModel(
            name='DraftJob',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contents', models.TextField(max_length=2000)),
                ('entity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='icf_entity.Entity')),
            ],
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-05-08 11:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('icf_generic', '0012_auto_20190207_1356'),
    ]

    operations = [
        migrations.AddField(
            model_name='faq',
            name='category',
            field=models.SmallIntegerField(blank=True, choices=[(2, 'job_sekeers'), (1, 'professional'), (3, 'entities')], null=True),
        ),
        migrations.AddField(
            model_name='faq',
            name='video_url',
            field=models.URLField(blank=True, null=True),
        ),
    ]

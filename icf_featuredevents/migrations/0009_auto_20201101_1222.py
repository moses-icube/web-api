# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2020-11-01 06:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('icf_featuredevents', '0008_featuredevent_email_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='featuredevent',
            name='email_content_en',
            field=models.TextField(default='', null=True, verbose_name='email_content'),
        ),
        migrations.AddField(
            model_name='featuredevent',
            name='email_content_es',
            field=models.TextField(default='', null=True, verbose_name='email_content'),
        ),
        migrations.AddField(
            model_name='featuredevent',
            name='email_content_fr',
            field=models.TextField(default='', null=True, verbose_name='email_content'),
        ),
    ]

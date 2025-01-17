# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-01-02 07:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SentGroupSms',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('messages', models.CharField(blank=True, max_length=1000, null=True)),
                ('messages_en', models.CharField(blank=True, max_length=1000, null=True)),
                ('messages_fr', models.CharField(blank=True, max_length=1000, null=True)),
                ('messages_es', models.CharField(blank=True, max_length=1000, null=True)),
                ('sent_at', models.DateTimeField(auto_now=True)),
                ('success_count', models.IntegerField(default=0)),
                ('failure_count', models.IntegerField(default=0)),
            ],
            options={
                'verbose_name_plural': 'Send Group Sms',
            },
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-06-11 12:11
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('icf_jobs', '0011_unregistereduserfileupload'),
    ]

    operations = [
        migrations.RenameField(
            model_name='unregistereduserfileupload',
            old_name='phone',
            new_name='mobile',
        ),
    ]
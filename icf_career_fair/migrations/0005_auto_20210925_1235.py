# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2021-09-25 07:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('icf_career_fair', '0004_auto_20210923_1121'),
    ]

    operations = [
        migrations.RenameField(
            model_name='careerfairmarkedfordelete',
            old_name='event',
            new_name='career_fair',
        ),
        migrations.AddField(
            model_name='speaker',
            name='speaker_type',
            field=models.SmallIntegerField(choices=[(1, 'Speaker'), (2, 'Keynote_speaker'), (3, 'Panelist'), (4, 'Host'), (5, 'Presenter')], default=1),
        ),
        migrations.AddField(
            model_name='speakeroptional',
            name='speaker_type',
            field=models.SmallIntegerField(choices=[(1, 'Speaker'), (2, 'Keynote_speaker'), (3, 'Panelist'), (4, 'Host'), (5, 'Presenter')], default=1),
        ),
    ]

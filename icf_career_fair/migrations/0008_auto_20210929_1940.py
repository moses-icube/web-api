# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2021-09-29 14:10
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('icf_career_fair', '0007_participant_participantandproduct'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Participant',
            new_name='CareerFairParticipant',
        ),
    ]
# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-11-21 13:02
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('icf_entity', '0005_pending_entityuser'),
    ]

    operations = [
        migrations.CreateModel(
            name='PendingEntityUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now=True)),
                ('entity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='icf_entity.Entity')),
                ('entity_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pending_entity_user', to=settings.AUTH_USER_MODEL)),
                ('user_to_add', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='pending_entityuser',
            name='entity',
        ),
        migrations.RemoveField(
            model_name='pending_entityuser',
            name='user',
        ),
        migrations.DeleteModel(
            name='Pending_EntityUser',
        ),
    ]

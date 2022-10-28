# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-07-17 12:18
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('icf_generic', '0017_address_address_type'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('icf_orders', '0003_auto_20190717_1437'),
    ]

    operations = [
        migrations.CreateModel(
            name='BillingAddress',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=200, null=True)),
                ('last_name', models.CharField(blank=True, max_length=200, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('address', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='icf_generic.Address')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-11-21 11:16
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('icf_generic', '0004_auto_20181119_1249'),
        ('icf_item', '0004_itemdraft'),
        ('icf_jobs', '0004_draftjob'),
    ]

    operations = [
        migrations.CreateModel(
            name='JobDraft',
            fields=[
                ('itemdraft_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='icf_item.ItemDraft')),
                ('experience_years', models.SmallIntegerField(blank=True, choices=[(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10), (11, 11), (12, 12), (13, 13), (14, 14), (15, 15), (16, 16), (17, 17), (18, 18), (19, 19), (20, 20), (21, 21), (22, 22), (23, 23), (24, 24), (25, 25), (26, 26), (27, 27), (28, 28), (29, 29), (30, 30), (31, 31), (32, 32), (33, 33), (34, 34), (35, 35), (36, 36), (37, 37), (38, 38), (39, 39), (40, 40)], null=True)),
                ('experience_months', models.SmallIntegerField(blank=True, choices=[(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10), (11, 11), (12, 12)], null=True)),
                ('salary', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True)),
                ('salary_is_public', models.BooleanField(default=False)),
                ('open_positions', models.SmallIntegerField(default=1)),
                ('education_level', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='icf_jobs.EducationLevel')),
                ('job_type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='icf_jobs.JobType')),
                ('occupation', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='icf_jobs.Occupation')),
                ('salary_currency', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='icf_generic.Currency')),
                ('salary_frequency', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='icf_jobs.SalaryFrequency')),
            ],
            options={
                'verbose_name_plural': 'Jobs',
                'ordering': ['-created'],
            },
            bases=('icf_item.itemdraft',),
        ),
    ]

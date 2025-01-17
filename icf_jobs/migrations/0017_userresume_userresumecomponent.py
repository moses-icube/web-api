# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-09-24 07:07
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import icf_jobs.models


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('icf_jobs', '0016_auto_20190918_1449'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserResume',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=500, null=True, verbose_name='title')),
                ('thumbnail', models.ImageField(blank=True, null=True, upload_to=icf_jobs.models.upload_dynamic_resume_thumbnail_media_location)),
                ('resume', models.FileField(blank=True, max_length=200, null=True, upload_to=icf_jobs.models.upload_dynamic_resume_media_location, validators=[icf_jobs.models.validate_file_extension])),
                ('biography', models.CharField(blank=True, max_length=250, null=True, verbose_name='biography')),
                ('slug', models.SlugField(blank=True, unique=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('job_profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='icf_jobs.UserJobProfile')),
            ],
        ),
        migrations.CreateModel(
            name='UserResumeComponent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('object_id', models.PositiveIntegerField()),
                ('is_active', models.BooleanField(default=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.ContentType')),
                ('user_resume', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='icf_jobs.UserResume')),
            ],
        ),
    ]

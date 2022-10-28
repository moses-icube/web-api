# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-09-11 06:59
from __future__ import unicode_literals

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('icf_generic', '0017_address_address_type'),
        ('contenttypes', '0002_remove_content_type_name'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('icf_jobs', '0012_auto_20190611_1741'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reference',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, verbose_name='name')),
                ('position', models.CharField(blank=True, max_length=100, verbose_name='position')),
                ('phone', models.CharField(blank=True, max_length=25, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.", regex='^\\+?1?\\d{9,15}$')])),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('object_id', models.PositiveIntegerField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.ContentType')),
            ],
            options={
                'verbose_name_plural': 'References',
            },
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=2000, verbose_name='description')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Tasks',
            },
        ),
        migrations.CreateModel(
            name='UserHobbie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hobbie', models.CharField(max_length=500, verbose_name='hobbie')),
                ('job_profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='icf_jobs.UserJobProfile')),
            ],
            options={
                'verbose_name_plural': 'UserHobbies',
            },
        ),
        migrations.CreateModel(
            name='UserProject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500, verbose_name='title')),
                ('summary', models.TextField(max_length=50000, verbose_name='summary')),
                ('start_date', models.DateField(verbose_name='start date')),
                ('end_date', models.DateField(verbose_name='end date')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='icf_generic.City')),
                ('job_profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='icf_jobs.UserJobProfile')),
            ],
        ),
        migrations.CreateModel(
            name='UserRelevantLink',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('relevant_link', models.URLField()),
                ('job_profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='icf_jobs.UserJobProfile')),
            ],
            options={
                'verbose_name_plural': 'UserRelevantLinks',
            },
        ),
        migrations.AddField(
            model_name='usereducation',
            name='city',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='icf_generic.City'),
        ),
        migrations.AddField(
            model_name='userskill',
            name='expertise',
            field=models.SmallIntegerField(choices=[(1, 'Beginner'), (2, 'Novice'), (3, 'Intermediate'), (4, 'Advanced'), (5, 'Expert')], default=1),
        ),
        migrations.AddField(
            model_name='userworkexperience',
            name='city',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='icf_generic.City'),
        ),
        migrations.AddField(
            model_name='task',
            name='work_experience',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='icf_jobs.UserWorkExperience'),
        ),
    ]

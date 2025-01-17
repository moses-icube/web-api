# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-10-31 06:36
from __future__ import unicode_literals

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import icf_entity.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CompanySize',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size', models.CharField(blank=True, max_length=40, unique=True)),
                ('description', models.CharField(blank=True, max_length=80)),
            ],
            options={
                'ordering': ('size',),
                'verbose_name_plural': 'CompanySizes',
            },
        ),
        migrations.CreateModel(
            name='Entity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True, verbose_name='name')),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=25, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.", regex='^\\+?1?\\d{9,15}$')])),
                ('alternate_phone', models.CharField(blank=True, max_length=25, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.", regex='^\\+?1?\\d{9,15}$')])),
                ('website', models.URLField(blank=True)),
                ('description', models.CharField(max_length=1000, verbose_name='description')),
                ('status', models.SmallIntegerField(choices=[(2, 'Active'), (3, 'Inactive')], default=1)),
                ('slug', models.SlugField(blank=True, max_length=200)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('linked_in', models.URLField(blank=True)),
                ('twitter', models.URLField(blank=True)),
            ],
            options={
                'ordering': ['-created'],
                'permissions': (('icf_ent_cr', 'entity create'), ('icf_ent_ed', 'ability to change entity'), ('icf_ent_adm', 'act as admin of entity'), ('icf_ent_add_usr', 'ability to add entity user'), ('icf_ent_usr', 'ability to view entity')),
            },
        ),
        migrations.CreateModel(
            name='EntityUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('entity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='icf_entity.Entity')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='FeaturedEntity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='title')),
                ('description', models.CharField(max_length=150, verbose_name='description')),
                ('start_date', models.DateTimeField()),
                ('end_date', models.DateTimeField()),
                ('status', models.SmallIntegerField(choices=[(1, 'Active'), (2, 'Inactive')], default=2)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('entity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='icf_entity.Entity')),
            ],
        ),
        migrations.CreateModel(
            name='Industry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('industry', models.CharField(blank=True, max_length=200, unique=True)),
                ('industry_en', models.CharField(blank=True, max_length=200, null=True, unique=True)),
                ('industry_fr', models.CharField(blank=True, max_length=200, null=True, unique=True)),
                ('industry_es', models.CharField(blank=True, max_length=200, null=True, unique=True)),
                ('description', models.CharField(blank=True, max_length=500)),
                ('description_en', models.CharField(blank=True, max_length=500, null=True)),
                ('description_fr', models.CharField(blank=True, max_length=500, null=True)),
                ('description_es', models.CharField(blank=True, max_length=500, null=True)),
            ],
            options={
                'ordering': ('industry',),
                'verbose_name_plural': 'Industries',
            },
        ),
        migrations.CreateModel(
            name='Logo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(height_field='height', upload_to=icf_entity.models.upload_entity_media_location, width_field='width')),
                ('height', models.PositiveIntegerField(null=True)),
                ('width', models.PositiveIntegerField(null=True)),
                ('entity', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='logo', to='icf_entity.Entity')),
            ],
        ),
        migrations.CreateModel(
            name='Sector',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sector', models.CharField(blank=True, max_length=80, unique=True)),
                ('sector_en', models.CharField(blank=True, max_length=80, null=True, unique=True)),
                ('sector_fr', models.CharField(blank=True, max_length=80, null=True, unique=True)),
                ('sector_es', models.CharField(blank=True, max_length=80, null=True, unique=True)),
                ('description', models.CharField(blank=True, max_length=500)),
                ('description_en', models.CharField(blank=True, max_length=500, null=True)),
                ('description_fr', models.CharField(blank=True, max_length=500, null=True)),
                ('description_es', models.CharField(blank=True, max_length=500, null=True)),
            ],
            options={
                'ordering': ('sector',),
                'verbose_name_plural': 'Sectors',
            },
        ),
        migrations.CreateModel(
            name='TeamMember',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='name')),
                ('position', models.CharField(max_length=50, verbose_name='position')),
                ('image', models.ImageField(height_field='height', upload_to=icf_entity.models.upload_entity_media_location, width_field='width')),
                ('height', models.PositiveIntegerField(null=True)),
                ('width', models.PositiveIntegerField(null=True)),
                ('is_incharge', models.BooleanField(default=False)),
                ('featured_entity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='icf_entity.FeaturedEntity')),
            ],
        ),
    ]

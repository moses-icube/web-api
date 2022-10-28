# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-08-30 07:47
from __future__ import unicode_literals

from django.db import migrations, models
import icf_events.models


class Migration(migrations.Migration):

    dependencies = [
        ('icf_events', '0010_auto_20190829_1927'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='eventgalleryoptional',
            name='gallery_url',
        ),
        migrations.RemoveField(
            model_name='eventgalleryoptional',
            name='hero_image',
        ),
        migrations.RemoveField(
            model_name='eventgalleryoptional',
            name='image_1',
        ),
        migrations.RemoveField(
            model_name='eventgalleryoptional',
            name='image_2',
        ),
        migrations.RemoveField(
            model_name='eventgalleryoptional',
            name='image_3',
        ),
        migrations.RemoveField(
            model_name='eventgalleryoptional',
            name='image_4',
        ),
        migrations.RemoveField(
            model_name='eventgalleryoptional',
            name='is_hero_image',
        ),
        migrations.RemoveField(
            model_name='eventgalleryoptional',
            name='title',
        ),
        migrations.AddField(
            model_name='eventgalleryoptional',
            name='image',
            field=models.ImageField(default=1, upload_to=icf_events.models.upload_event_media_location),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='eventgalleryoptional',
            name='image_type',
            field=models.SmallIntegerField(choices=[(1, 'Hero'), (2, 'Gallery')], default=2),
        ),
        migrations.AlterField(
            model_name='eventgalleryoptional',
            name='event_slug',
            field=models.CharField(max_length=150),
        ),
    ]
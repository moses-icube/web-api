# Generated by Django 3.2.14 on 2022-08-25 04:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('icf_jobs', '0027_auto_20220825_0420'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userreference',
            name='entity',
        ),
        migrations.RemoveField(
            model_name='userreference',
            name='phone',
        ),
    ]
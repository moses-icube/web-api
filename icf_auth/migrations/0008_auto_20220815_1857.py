# Generated by Django 3.2.14 on 2022-08-15 18:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('icf_auth', '0007_auto_20200610_0602'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='professional_pronoun',
            field=models.CharField(max_length=250, null=True, verbose_name='professional_pronoun'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='professional_title',
            field=models.CharField(max_length=250, null=True, verbose_name='professional_title'),
        ),
        migrations.AlterField(
            model_name='user',
            name='first_name',
            field=models.CharField(blank=True, max_length=150, verbose_name='first name'),
        ),
        migrations.AlterField(
            model_name='user',
            name='last_name',
            field=models.CharField(blank=True, max_length=150, verbose_name='last name'),
        ),
    ]

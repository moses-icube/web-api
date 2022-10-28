# Generated by Django 3.2.14 on 2022-08-28 17:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('icf_generic', '0021_auto_20200121_1138'),
        ('icf_announcement', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='announcement',
            name='button_text',
            field=models.CharField(blank=True, max_length=170, null=True, verbose_name='button_text'),
        ),
        migrations.AddField(
            model_name='announcement',
            name='country',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='icf_generic.country'),
        ),
        migrations.AlterField(
            model_name='announcement',
            name='url',
            field=models.CharField(blank=True, max_length=170, null=True, verbose_name='url'),
        ),
    ]
# Generated by Django 3.2.14 on 2022-08-31 23:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('icf_generic', '0021_auto_20200121_1138'),
        ('icf_jobs', '0031_usercourse'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserFreelanceService',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500, verbose_name='name')),
                ('service_description', models.TextField(blank=True, null=True, verbose_name='service_description')),
                ('deliverable_description', models.TextField(blank=True, null=True, verbose_name='deliverable_description')),
                ('price_min', models.IntegerField(verbose_name='price_min')),
                ('price_max', models.IntegerField(verbose_name='price_max')),
                ('delivery_min', models.IntegerField(verbose_name='delivery_min')),
                ('delivery_max', models.IntegerField(verbose_name='delivery_max')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='icf_generic.category')),
                ('currency', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='icf_generic.currency')),
                ('delivery_time', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='icf_jobs.salaryfrequency')),
                ('job_profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='icf_jobs.userjobprofile')),
            ],
            options={
                'verbose_name_plural': 'UserFreelanceServices',
            },
        ),
    ]

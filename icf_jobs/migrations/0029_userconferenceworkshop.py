# Generated by Django 3.2.14 on 2022-08-30 15:55

from django.db import migrations, models
import django.db.models.deletion
import icf_generic.fields


class Migration(migrations.Migration):

    dependencies = [
        ('icf_generic', '0021_auto_20200121_1138'),
        ('icf_jobs', '0028_auto_20220825_0458'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserConferenceWorkshop',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500, verbose_name='name')),
                ('organizer', models.CharField(blank=True, max_length=250, null=True, verbose_name='organizer')),
                ('description', models.TextField(max_length=50000, verbose_name='description')),
                ('start_date', icf_generic.fields.ICFApproxDateField()),
                ('end_date', icf_generic.fields.ICFApproxDateField()),
                ('role', models.SmallIntegerField(choices=[(1, 'Paticipant'), (2, 'Moderator')], default=1)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='icf_generic.city')),
                ('job_profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='icf_jobs.userjobprofile')),
            ],
            options={
                'verbose_name_plural': 'UserConferenceWorkshop',
            },
        ),
    ]

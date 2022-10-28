# Generated by Django 3.2.14 on 2022-08-25 04:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import icf_messages.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('icf_messages', '0007_auto_20220815_1857'),
    ]

    operations = [
        migrations.CreateModel(
            name='MessageAttachmentUpload',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attachment_src', models.FileField(max_length=200, upload_to=icf_messages.models.upload_message_attachment_location, validators=[icf_messages.models.validate_file_extension])),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
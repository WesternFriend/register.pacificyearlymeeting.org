# Generated by Django 2.2.9 on 2020-02-01 19:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0002_registrant_memorial_meeting_only'),
    ]

    operations = [
        migrations.RenameField(
            model_name='registrant',
            old_name='memorial_meeting_only',
            new_name='attending_memorial_meeting_only',
        ),
    ]
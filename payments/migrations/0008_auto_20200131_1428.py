# Generated by Django 2.2.9 on 2020-01-31 14:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0005_registrationpage_intro'),
        ('payments', '0007_auto_20200113_1736'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='RegistrantPayment',
            new_name='Allocation',
        ),
    ]
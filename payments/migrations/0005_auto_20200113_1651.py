# Generated by Django 2.2.9 on 2020-01-13 16:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0004_payment_payee'),
    ]

    operations = [
        migrations.RenameField(
            model_name='payment',
            old_name='payee',
            new_name='paid_by',
        ),
    ]
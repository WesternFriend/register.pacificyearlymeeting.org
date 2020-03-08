# Generated by Django 2.2.9 on 2020-02-22 17:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0013_editregistrantpage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registrant',
            name='overnight_accommodations',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='fees.AccommodationFee'),
        ),
    ]
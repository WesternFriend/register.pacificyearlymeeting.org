# Generated by Django 2.2.9 on 2020-02-01 17:35

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProgramChoice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('age_min', models.IntegerField(validators=[django.core.validators.MinValueValidator(0)])),
                ('age_max', models.IntegerField(validators=[django.core.validators.MinValueValidator(0)])),
            ],
            options={
                'db_table': 'program_choice',
            },
        ),
    ]

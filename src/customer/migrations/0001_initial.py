# Generated by Django 3.0.5 on 2020-05-08 04:56

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('mobile_number', models.IntegerField()),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('car_company', models.CharField(choices=[('tata', 'Tata'), ('maruti', 'Maruti'), ('mahindra', 'Mahindra'), ('bmw', 'BMW')], max_length=20)),
                ('car_fuel', models.CharField(choices=[('petrol', 'Petrol'), ('diesel', 'Diesel'), ('natural_gas', 'Natural Gas'), ('hydrogen', 'Hydrogen')], max_length=20)),
                ('car_year', models.PositiveIntegerField(validators=[django.core.validators.MaxValueValidator(9999)])),
            ],
        ),
    ]

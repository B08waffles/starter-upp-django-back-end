# Generated by Django 4.0.3 on 2022-05-11 13:35

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('starterupperupp', '0007_alter_transaction_amount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='amount',
            field=models.FloatField(max_length=55, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(999999999999)]),
        ),
    ]

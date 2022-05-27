# Generated by Django 4.0.3 on 2022-05-26 11:21

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('starterupperupp', '0008_alter_transaction_amount'),
    ]

    operations = [
        migrations.CreateModel(
            name='PayRates',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now=True)),
                ('pay_rate', models.FloatField(max_length=55, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(9999)])),
                ('associated_company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='the_associated_company', to='starterupperupp.company', to_field='company_name')),
                ('associated_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='the_associated_user', to=settings.AUTH_USER_MODEL, to_field='username')),
            ],
        ),
    ]

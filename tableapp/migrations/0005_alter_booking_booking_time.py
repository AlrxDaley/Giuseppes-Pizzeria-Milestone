# Generated by Django 4.0.2 on 2022-07-28 10:51

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('tableapp', '0004_contact_booking_booking_time_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='booking_time',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]

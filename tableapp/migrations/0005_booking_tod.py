# Generated by Django 4.0.2 on 2022-08-03 17:41

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('tableapp', '0004_contact_alter_booking_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='booking_ToD',
            field=models.DateTimeField(default=django.utils.timezone.now, max_length=255),
        ),
    ]

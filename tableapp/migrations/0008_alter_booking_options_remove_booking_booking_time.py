# Generated by Django 4.0.2 on 2022-08-03 17:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tableapp', '0007_alter_booking_options_remove_booking_booking_date'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='booking',
            options={'ordering': ['-order_id']},
        ),
    ]

# Generated by Django 4.0.2 on 2022-08-03 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tableapp', '0004_contact_alter_booking_booking_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='phone_number',
            field=models.CharField(max_length=1024),
        ),
        migrations.AlterField(
            model_name='booking',
            name='special_request',
            field=models.TextField(blank=True, max_length=1024),
        ),
    ]

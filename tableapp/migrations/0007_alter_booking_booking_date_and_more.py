# Generated by Django 4.0.2 on 2022-07-30 10:50

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('tableapp', '0006_alter_booking_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='booking_date',
            field=models.DateTimeField(default=django.utils.timezone.now, max_length=2550),
        ),
        migrations.AlterField(
            model_name='booking',
            name='booking_time',
            field=models.DateTimeField(default=django.utils.timezone.now, max_length=2550),
        ),
        migrations.AlterField(
            model_name='booking',
            name='first_name',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='booking',
            name='last_name',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='booking',
            name='order_id',
            field=models.CharField(blank=True, max_length=1200),
        ),
        migrations.AlterField(
            model_name='booking',
            name='phone_number',
            field=models.CharField(max_length=100),
        ),
    ]

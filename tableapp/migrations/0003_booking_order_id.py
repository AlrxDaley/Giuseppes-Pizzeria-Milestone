# Generated by Django 4.0.2 on 2022-03-28 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tableapp', '0002_alter_booking_booking_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='order_id',
            field=models.CharField(blank=True, max_length=120),
        ),
    ]
# Generated by Django 5.0.3 on 2024-05-08 03:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booklist', '0008_device_analog_value_device_digital_value_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='device',
            name='id',
            field=models.UUIDField(primary_key=True, serialize=False),
        ),
    ]

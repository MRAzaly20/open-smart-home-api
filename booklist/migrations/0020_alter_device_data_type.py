# Generated by Django 5.0.3 on 2024-05-23 06:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booklist', '0019_device_data_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='device',
            name='data_type',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]

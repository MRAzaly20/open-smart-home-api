# Generated by Django 5.0.3 on 2024-03-22 02:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('booklist', '0005_alter_userprofile_user'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='userprofile',
            options={'ordering': ['phone_number'], 'verbose_name': 'user_profile', 'verbose_name_plural': 'user_profile'},
        ),
    ]

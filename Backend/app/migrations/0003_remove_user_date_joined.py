# Generated by Django 5.0.6 on 2024-07-11 00:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_rename_first_name_user_username_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='date_joined',
        ),
    ]

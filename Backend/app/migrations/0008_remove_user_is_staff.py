# Generated by Django 5.0.6 on 2024-07-16 01:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_rename_is_admin_user_is_staff'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='is_staff',
        ),
    ]

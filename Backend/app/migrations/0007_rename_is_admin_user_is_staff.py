# Generated by Django 5.0.6 on 2024-07-16 00:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_user_is_admin'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='is_admin',
            new_name='is_staff',
        ),
    ]
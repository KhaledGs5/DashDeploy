# Generated by Django 5.0.6 on 2024-08-05 18:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0014_component_value'),
    ]

    operations = [
        migrations.AlterField(
            model_name='component',
            name='value',
            field=models.IntegerField(),
        ),
    ]

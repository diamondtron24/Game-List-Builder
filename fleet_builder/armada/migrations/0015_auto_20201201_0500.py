# Generated by Django 3.1.2 on 2020-12-01 05:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('armada', '0014_auto_20201201_0453'),
    ]

    operations = [
        migrations.RenameField(
            model_name='baseship',
            old_name='ordinance_1',
            new_name='ordnance_1',
        ),
        migrations.RenameField(
            model_name='baseship',
            old_name='ordinance_2',
            new_name='ordnance_2',
        ),
    ]
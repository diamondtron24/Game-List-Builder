# Generated by Django 3.1.2 on 2020-11-17 05:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('armada', '0002_auto_20201117_0514'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ship',
            name='points',
            field=models.IntegerField(),
        ),
    ]
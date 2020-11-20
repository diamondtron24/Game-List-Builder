# Generated by Django 3.1.2 on 2020-11-19 01:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('armada', '0008_auto_20201118_0525'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ship',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('ship', models.ManyToManyField(related_name='saved_ship', to='armada.BaseShip')),
                ('upgrades', models.ManyToManyField(related_name='ships_including_these_upgrades', to='armada.Upgrade')),
            ],
        ),
    ]

# Generated by Django 4.2.1 on 2023-05-10 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0019_diecast_inventory'),
    ]

    operations = [
        migrations.AddField(
            model_name='diecast',
            name='sold',
            field=models.IntegerField(default=0),
        ),
    ]

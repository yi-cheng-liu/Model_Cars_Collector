# Generated by Django 4.2.1 on 2023-05-10 07:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0016_diecast_content_type'),
    ]

    operations = [
        migrations.RenameField(
            model_name='diecast',
            old_name='year',
            new_name='production_year',
        ),
    ]

# Generated by Django 4.2.1 on 2023-05-13 19:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0034_carouselitem'),
    ]

    operations = [
        migrations.AddField(
            model_name='diecast',
            name='on_sale_home',
            field=models.BooleanField(default=False),
        ),
    ]

# Generated by Django 4.2.1 on 2023-05-14 18:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0037_diecast_save_percent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='diecast',
            name='on_sale',
            field=models.BooleanField(default=False, help_text='ON SALE: 2, 4, 6, 8 items'),
        ),
        migrations.AlterField(
            model_name='diecast',
            name='on_sale_home',
            field=models.BooleanField(default=False, help_text='ON SALE on home page: Max 2 items'),
        ),
    ]

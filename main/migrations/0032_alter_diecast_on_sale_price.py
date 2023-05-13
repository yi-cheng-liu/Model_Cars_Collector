# Generated by Django 4.2.1 on 2023-05-12 21:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0031_manufacturer_important'),
    ]

    operations = [
        migrations.AlterField(
            model_name='diecast',
            name='on_sale_price',
            field=models.DecimalField(blank=True, decimal_places=2, help_text='ON SALE: on sale price < retail price', max_digits=7, null=True),
        ),
    ]

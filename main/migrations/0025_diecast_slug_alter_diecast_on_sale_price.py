# Generated by Django 4.2.1 on 2023-05-11 21:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0024_diecast_on_sale_price_manufacturer_slug_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='diecast',
            name='slug',
            field=models.SlugField(blank=True, default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='diecast',
            name='on_sale_price',
            field=models.DecimalField(decimal_places=2, help_text='ON SALE: on sale price < retail price', max_digits=7, null=True),
        ),
    ]

# Generated by Django 4.2.1 on 2023-05-09 21:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_rename_vehicle_brand_vehiclebrand'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productattribute',
            name='product',
        ),
        migrations.DeleteModel(
            name='Product',
        ),
        migrations.DeleteModel(
            name='ProductAttribute',
        ),
    ]

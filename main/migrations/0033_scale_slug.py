# Generated by Django 4.2.1 on 2023-05-13 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0032_alter_diecast_on_sale_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='scale',
            name='slug',
            field=models.SlugField(blank=True, default='', help_text="DON'T NEED TO FILL IN", max_length=255),
        ),
    ]

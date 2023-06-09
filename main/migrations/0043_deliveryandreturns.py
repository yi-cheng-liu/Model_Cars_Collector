# Generated by Django 4.2.1 on 2023-06-27 21:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0042_aboutus_picture'),
    ]

    operations = [
        migrations.CreateModel(
            name='DeliveryAndReturns',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Delivery and returns', max_length=30)),
                ('text1', models.TextField(blank=True, null=True)),
                ('text2', models.TextField(blank=True, null=True)),
                ('text3', models.TextField(blank=True, null=True)),
                ('picture', models.ImageField(blank=True, null=True, upload_to='manufacturer/')),
            ],
        ),
    ]

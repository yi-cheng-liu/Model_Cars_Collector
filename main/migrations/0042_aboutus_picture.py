# Generated by Django 4.2.1 on 2023-05-16 00:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0041_rename_text_aboutus_text1_aboutus_text2_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='aboutus',
            name='picture',
            field=models.ImageField(blank=True, null=True, upload_to='manufacturer/'),
        ),
    ]

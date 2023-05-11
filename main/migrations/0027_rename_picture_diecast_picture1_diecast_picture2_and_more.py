# Generated by Django 4.2.1 on 2023-05-11 21:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0026_vehiclebrand_slug_alter_diecast_slug_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='diecast',
            old_name='picture',
            new_name='picture1',
        ),
        migrations.AddField(
            model_name='diecast',
            name='picture2',
            field=models.ImageField(blank=True, null=True, upload_to='pictures/'),
        ),
        migrations.AddField(
            model_name='diecast',
            name='picture3',
            field=models.ImageField(blank=True, null=True, upload_to='pictures/'),
        ),
        migrations.AddField(
            model_name='diecast',
            name='picture4',
            field=models.ImageField(blank=True, null=True, upload_to='pictures/'),
        ),
    ]
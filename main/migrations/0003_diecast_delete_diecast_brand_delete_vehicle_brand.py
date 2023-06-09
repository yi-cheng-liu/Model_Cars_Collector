# Generated by Django 4.2 on 2023-04-11 21:22

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0002_vehicle_brand"),
    ]

    operations = [
        migrations.CreateModel(
            name="diecast",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "title",
                    models.CharField(
                        max_length=100,
                        validators=[
                            django.core.validators.MinLengthValidator(
                                5, "Title must be greater than 2 characters"
                            ),
                            django.core.validators.MaxLengthValidator(
                                100, "Title must be less than 1 characters"
                            ),
                        ],
                    ),
                ),
                (
                    "vehicle_name",
                    models.CharField(
                        max_length=50,
                        validators=[
                            django.core.validators.MinLengthValidator(
                                2, "Vehicle must be greater than 2 characters"
                            ),
                            django.core.validators.MaxLengthValidator(
                                30, "Vehicle must be less than 1 characters"
                            ),
                        ],
                    ),
                ),
                (
                    "manufacturer",
                    models.CharField(
                        max_length=30,
                        validators=[
                            django.core.validators.MinLengthValidator(
                                2, "Manufacturer must be greater than 2 characters"
                            ),
                            django.core.validators.MaxLengthValidator(
                                30, "Manufacturer must be less than 30 characters"
                            ),
                        ],
                    ),
                ),
                (
                    "vehicle_brand",
                    models.CharField(
                        max_length=30,
                        validators=[
                            django.core.validators.MinLengthValidator(
                                2, "Brand must be greater than 2 characters"
                            ),
                            django.core.validators.MaxLengthValidator(
                                30, "Brand must be less than 30 characters"
                            ),
                        ],
                    ),
                ),
                ("scale", models.CharField(max_length=5)),
                (
                    "price",
                    models.DecimalField(decimal_places=2, max_digits=7, null=True),
                ),
                (
                    "year",
                    models.IntegerField(
                        default=2023,
                        validators=[
                            django.core.validators.MinValueValidator(1800),
                            django.core.validators.MaxValueValidator(2023),
                        ],
                    ),
                ),
                ("color", models.CharField(max_length=15)),
                ("text", models.TextField()),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("picture", models.BinaryField(editable=True, null=True)),
                (
                    "content_type",
                    models.CharField(
                        help_text="The MIMEType of the file", max_length=256, null=True
                    ),
                ),
                ("image", models.ImageField(upload_to="diecast_brand_img/")),
            ],
        ),
        migrations.DeleteModel(
            name="Diecast_Brand",
        ),
        migrations.DeleteModel(
            name="Vehicle_Brand",
        ),
    ]

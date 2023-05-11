from django.db import models
from django.core.validators import MinLengthValidator, MaxLengthValidator, MinValueValidator, MaxValueValidator
from django.core.exceptions import ValidationError
from django.conf import settings
from django.utils.text import slugify

from datetime import datetime

current_year = datetime.now().year


class Manufacturer(models.Model):
    name = models.CharField(max_length=30,
        validators=[MinLengthValidator(2, "Manufacturer must be greater than 2 characters"),
                    MaxLengthValidator(30, "Manufacturer must be less than 30 characters")])
    slug = models.SlugField(max_length=255, default='', blank=True, help_text="DON'T NEED TO FILL IN")
    # Picture
    picture = models.ImageField(upload_to='manufacturer/', null=True, blank=True)

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

class VehicleBrand(models.Model):
    name = models.CharField(max_length=30,
        validators=[MinLengthValidator(2, "Manufacturer must be greater than 2 characters"),
                    MaxLengthValidator(30, "Manufacturer must be less than 30 characters")])
    slug = models.SlugField(max_length=255, default='', blank=True, help_text="DON'T NEED TO FILL IN")
    
    # Picture
    picture = models.ImageField(upload_to='brand/', null=True, blank=True)

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)
    
class Scale(models.Model):
    name = models.CharField(max_length=5)
    def __str__(self):
        return self.name

class Diecast(models.Model):
    title = models.CharField(max_length=100, 
                    validators=[MinLengthValidator(5, "Title must be greater than 2 characters"),
                                MaxLengthValidator(100, "Title must be less than 1 characters")])
    vehicle_name = models.CharField(max_length=50, 
                    validators=[MinLengthValidator(2, "Vehicle must be greater than 2 characters"),
                                MaxLengthValidator(50, "Vehicle must be less than 1 characters")])
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    vehicle_brand = models.ForeignKey(VehicleBrand, on_delete=models.CASCADE)
    scale = models.ForeignKey(Scale, on_delete=models.CASCADE)
    buying_price = models.DecimalField(max_digits=7, decimal_places=2, null=True)
    retail_price = models.DecimalField(max_digits=7, decimal_places=2, null=True)
    on_sale = models.BooleanField(default=False)
    on_sale_price = models.DecimalField(max_digits=7, decimal_places=2, null=True, help_text="ON SALE: on sale price < retail price")
    production_year = models.IntegerField(default=current_year,
            validators=[MinValueValidator(1800), MaxValueValidator(current_year)])    
    color = models.CharField(max_length=15)
    text = models.TextField(null=True, blank=True)

    # Hidden information
    featured = models.BooleanField(default=False)
    inventory = models.IntegerField(default=1,
            validators=[MinValueValidator(1), MaxValueValidator(1000)])
    sold = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    # Picture
    picture1 = models.ImageField(upload_to='pictures/', null=True, blank=True)
    picture2 = models.ImageField(upload_to='pictures/', null=True, blank=True)
    picture3 = models.ImageField(upload_to='pictures/', null=True, blank=True)
    picture4 = models.ImageField(upload_to='pictures/', null=True, blank=True)

    # Slug
    slug = models.SlugField(max_length=255, default='', blank=True, help_text="DON'T NEED TO FILL IN")
    
    def __str__(self) -> str:
        return self.title
    
    def is_valid_on_sale_price(self):
        if self.on_sale and self.on_sale_price and self.retail_price and self.on_sale_price >= self.retail_price:
            raise ValidationError("The product is on sale!!! The on sale price must be lower than the retail price.")
    
    def clean(self):
        super().clean()
        self.is_valid_on_sale_price()

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

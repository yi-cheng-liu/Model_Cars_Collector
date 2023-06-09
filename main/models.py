from django.db import models
from django.core.validators import MinLengthValidator, MaxLengthValidator, MinValueValidator, MaxValueValidator
from django.core.exceptions import ValidationError
from django.conf import settings
from django.utils import timezone
from django.utils.text import slugify
from django.contrib.auth.models import User
from datetime import datetime, timedelta
from decimal import Decimal

from payments import PurchasedItem
from payments.models import BasePayment
from pyparsing import Iterable

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)

    def __str__(self):
        return self.user.username

class Manufacturer(models.Model):
    name = models.CharField(max_length=30,
        validators=[MinLengthValidator(2, "Manufacturer must be greater than 2 characters"),
                    MaxLengthValidator(30, "Manufacturer must be less than 30 characters")])
    slug = models.SlugField(max_length=255, default='', blank=True, help_text="DON'T NEED TO FILL IN")

    # Hidden information
    important = models.BooleanField(default=False)

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
    slug = models.SlugField(max_length=255, default='', blank=True, help_text="DON'T NEED TO FILL IN")

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

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
    on_sale = models.BooleanField(default=False, help_text="ON SALE: 2, 4, 6, 8 items")
    on_sale_home = models.BooleanField(default=False, help_text="ON SALE on home page: Max 2 items")
    on_sale_price = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank = True, help_text="ON SALE: on sale price < retail price")
    save_percent = models.IntegerField(null=True, blank=True, validators=[MaxValueValidator(99)])
    production_year = models.IntegerField(default=datetime.now().year,
            validators=[MinValueValidator(1800), MaxValueValidator(datetime.now().year)])    
    color = models.CharField(max_length=15)
    text = models.TextField(null=True, blank=True)

    # Hidden information
    featured = models.BooleanField(default=False)
    inventory = models.IntegerField(default=1,
            validators=[MinValueValidator(1), MaxValueValidator(1000)])
    sold = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    profiles = models.ManyToManyField(Profile, blank=True)
    
    # Picture
    picture1 = models.ImageField(upload_to='pictures/', null=True)
    picture2 = models.ImageField(upload_to='pictures/', null=True)
    picture3 = models.ImageField(upload_to='pictures/', null=True)
    picture4 = models.ImageField(upload_to='pictures/', null=True, blank=True)
    picture5 = models.ImageField(upload_to='pictures/', null=True, blank=True)
    picture6 = models.ImageField(upload_to='pictures/', null=True, blank=True)
    picture7 = models.ImageField(upload_to='pictures/', null=True, blank=True)
    picture8 = models.ImageField(upload_to='pictures/', null=True, blank=True)

    # Slug
    slug = models.SlugField(max_length=255, default='', blank=True, help_text="DON'T NEED TO FILL IN")
    
    def __str__(self) -> str:
        return self.title
    
    def is_valid_on_sale_price(self):
        if self.on_sale and self.on_sale_price and self.retail_price and self.on_sale_price >= self.retail_price:
            raise ValidationError("The product is on sale!!! The on sale price must be lower than the retail price.")
    
    def is_recent(self):
        three_months_ago = timezone.now() - timezone.timedelta(days=90)
        return self.created_at >= three_months_ago
    
    def calculate_save_percent(self):
        if self.on_sale_price and self.retail_price and not self.save_percent:
            difference = self.retail_price - self.on_sale_price
            self.save_percent = (difference / self.retail_price) * 100

    def calculate_on_sale_price(self):
        if self.save_percent and self.retail_price and not self.on_sale_price:
            discount_amount = Decimal(self.save_percent / 100) * self.retail_price
            self.on_sale_price = self.retail_price - discount_amount
    
    def clean(self):
        super().clean()
        self.is_valid_on_sale_price()
        self.calculate_save_percent()
        self.calculate_on_sale_price()

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)

        # Force on_sale_price to be the same as retail_price when on_sale is False
        if not self.on_sale:
            self.on_sale_price = self.retail_price

        self.calculate_save_percent()
        self.calculate_on_sale_price()
        super().save(*args, **kwargs)

class CarouselItem(models.Model):
    name = models.CharField(max_length=100)
    picture = models.ImageField(upload_to='carousel/', null=True)
    caption = models.CharField(max_length=255)

    def __str__(self):
        return self.caption
    
class AboutUs(models.Model):
    name = models.CharField(max_length=30, default='About Us')
    text1 = models.TextField(null=True, blank=True)
    text2 = models.TextField(null=True, blank=True)
    text3 = models.TextField(null=True, blank=True)

    # Picture
    picture = models.ImageField(upload_to='manufacturer/', null=True, blank=True)

    def __str__(self):
        return self.name
    
class DeliveryAndReturns(models.Model):
    name = models.CharField(max_length=30, default='Delivery and returns')
    text1 = models.TextField(null=True, blank=True)
    text2 = models.TextField(null=True, blank=True)
    text3 = models.TextField(null=True, blank=True)

    # Picture
    picture = models.ImageField(upload_to='manufacturer/', null=True, blank=True)

    def __str__(self):
        return self.name
    
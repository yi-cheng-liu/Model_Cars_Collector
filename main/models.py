from django.db import models
from django.core.validators import MinLengthValidator, MaxLengthValidator, MinValueValidator, MaxValueValidator
from django.conf import settings


from datetime import datetime

current_year = datetime.now().year

class Manufacturer(models.Model):
    name = models.CharField(max_length=30,
        validators=[MinLengthValidator(2, "Manufacturer must be greater than 2 characters"),
                    MaxLengthValidator(30, "Manufacturer must be less than 30 characters")])

    def __str__(self):
        return self.name

class VehicleBrand(models.Model):
    name = models.CharField(max_length=30,
        validators=[MinLengthValidator(2, "Manufacturer must be greater than 2 characters"),
                    MaxLengthValidator(30, "Manufacturer must be less than 30 characters")])

    def __str__(self):
        return self.name
class Scale(models.Model):
    name = models.CharField(max_length=5)
    def __str__(self):
        return self.name

# Diecast model
class Diecast(models.Model):
    title = models.CharField(max_length=100, 
                    validators=[MinLengthValidator(5, "Title must be greater than 2 characters"),
                                MaxLengthValidator(100, "Title must be less than 1 characters")])
    vehicle_name = models.CharField(max_length=50, 
                    validators=[MinLengthValidator(2, "Vehicle must be greater than 2 characters"),
                                MaxLengthValidator(30, "Vehicle must be less than 1 characters")])
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    vehicle_brand = models.ForeignKey(VehicleBrand, on_delete=models.CASCADE)
    scale = models.ForeignKey(Scale, on_delete=models.CASCADE)
    buying_price = models.DecimalField(max_digits=7, decimal_places=2, null=True)
    retail_price = models.DecimalField(max_digits=7, decimal_places=2, null=True)
    year = models.IntegerField(default=current_year,
            validators=[MinValueValidator(1800), MaxValueValidator(current_year)])    
    color = models.CharField(max_length=15)
    text = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    # Picture
    # picture = models.BinaryField(null=True, editable=True)
    # content_type = models.CharField(max_length=256, null=True, help_text='The MIMEType of the file')
    # image = models.ImageField(upload_to="diecast_brand_img/")
    
    def __str__(self) -> str:
        return self.title

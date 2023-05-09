from django.contrib import admin
from .models import Manufacturer, VehicleBrand, Scale, Diecast

@admin.register(Diecast)
class DiecastAdmin(admin.ModelAdmin):
    list_display = ('vehicle_name', 'manufacturer', 'vehicle_brand', 'scale', 'buying_price', 'retail_price')
    list_filter = ('manufacturer',)

@admin.register(Manufacturer)
class ManufacturerAdmin(admin.ModelAdmin):
    ordering = ('name',)

@admin.register(VehicleBrand)
class VehicleBrandAdmin(admin.ModelAdmin):
    ordering = ('name',)

@admin.register(Scale)
class ScaleAdmin(admin.ModelAdmin):
    ordering = ('name',)

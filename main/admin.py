from django import forms
from django.contrib import admin
from django.utils.html import format_html

from .models import Manufacturer, VehicleBrand, Scale, Diecast

class DiecastAdminForm(forms.ModelForm):
    class Meta:
        model = Diecast
        fields = '__all__'
        
@admin.register(Diecast)
class DiecastAdmin(admin.ModelAdmin):
    list_display = ('vehicle_name', 'manufacturer', 'vehicle_brand', 'scale', 'buying_price', 'retail_price', 'inventory', 'sold', 'featured', 'on_sale', 'picture_preview')
    list_filter = ('manufacturer','featured', 'on_sale',)
    search_fields = ['vehicle_name', 'manufacturer__name', 'vehicle_brand__name']
    
    form = DiecastAdminForm
    
    def picture_preview(self, obj):
        if obj.picture:
            return format_html('<img src="{}" height="80"/>', obj.picture.url)
        return None

    picture_preview.short_description = 'Picture Preview'
    picture_preview.allow_tags = True

    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)
        if 'picture' in request.FILES:
            obj.picture = request.FILES['picture']
            obj.save()

class ManufacturerAdminForm(forms.ModelForm):
    picture = forms.ImageField(required=False)
    class Meta:
        model = Manufacturer
        fields = '__all__'

@admin.register(Manufacturer)
class ManufacturerAdmin(admin.ModelAdmin):
    ordering = ('name',)
    form = ManufacturerAdminForm
    list_display = ('name', 'picture_preview')

    def picture_preview(self, obj):
        if obj.picture:
            return format_html('<img src="{}" height="80"/>', obj.picture.url)
        return None

    picture_preview.short_description = 'Logo'
    picture_preview.allow_tags = True

@admin.register(VehicleBrand)
class VehicleBrandAdmin(admin.ModelAdmin):
    ordering = ('name',)

@admin.register(Scale)
class ScaleAdmin(admin.ModelAdmin):
    ordering = ('name',)

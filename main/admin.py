from django import forms
from django.contrib import admin
from django.utils.html import format_html

from .models import Manufacturer, VehicleBrand, Scale, Diecast, CarouselItem

class DiecastAdminForm(forms.ModelForm):
    class Meta:
        model = Diecast
        fields = '__all__'
        
@admin.register(Diecast)
class DiecastAdmin(admin.ModelAdmin):
    list_display = ('vehicle_name', 'manufacturer', 'vehicle_brand', 'scale', 'retail_price', 'on_sale_price', 'inventory', 'sold', 'featured', 'on_sale', 'picture_preview')
    list_filter = ('manufacturer','featured', 'on_sale',)
    search_fields = ['vehicle_name', 'manufacturer__name', 'vehicle_brand__name']
    
    form = DiecastAdminForm
    
    def picture_preview(self, obj):
        if obj.picture1:
            return format_html('<img src="{}" height="80"/>', obj.picture1.url)
        return None

    picture_preview.short_description = 'Picture Preview'
    picture_preview.allow_tags = True

    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)
        if 'picture1' in request.FILES:
            obj.picture1 = request.FILES['picture1']
        if 'picture2' in request.FILES:
            obj.picture2 = request.FILES['picture2']
        if 'picture3' in request.FILES:
            obj.picture3 = request.FILES['picture3']
        if 'picture4' in request.FILES:
            obj.picture4 = request.FILES['picture4']
        if 'picture5' in request.FILES:
            obj.picture5 = request.FILES['picture5']
        if 'picture6' in request.FILES:
            obj.picture6 = request.FILES['picture6']
        if 'picture7' in request.FILES:
            obj.picture7 = request.FILES['picture7']
        if 'picture8' in request.FILES:
            obj.picture8 = request.FILES['picture8']
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

class VehicleBrandAdminForm(forms.ModelForm):
    picture = forms.ImageField(required=False)
    class Meta:
        model = VehicleBrand
        fields = '__all__'
@admin.register(VehicleBrand)
class VehicleBrandAdmin(admin.ModelAdmin):
    ordering = ('name',)
    form = VehicleBrandAdminForm
    list_display = ('name', 'picture_preview')

    def picture_preview(self, obj):
        if obj.picture:
            return format_html('<img src="{}" height="80"/>', obj.picture.url)
        return None

    picture_preview.short_description = 'Logo'
    picture_preview.allow_tags = True

@admin.register(Scale)
class ScaleAdmin(admin.ModelAdmin):
    ordering = ('name',)

class CarouselItemAdminForm(forms.ModelForm):
    picture = forms.ImageField(required=False)
    class Meta:
        model = CarouselItem
        fields = '__all__'
@admin.register(CarouselItem)
class CarouselItemAdmin(admin.ModelAdmin):
    ordering = ('name',)
    form = CarouselItemAdminForm
    list_display = ('name', 'picture_preview')

    def picture_preview(self, obj):
        if obj.picture:
            return format_html('<img src="{}" height="80"/>', obj.picture.url)
        return None

    picture_preview.short_description = 'Carousel Picture'
    picture_preview.allow_tags = True

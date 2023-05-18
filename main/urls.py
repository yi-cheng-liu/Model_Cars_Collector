from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('manufacturer-list/', views.manufacturer_list, name='manufacturer-list'),
    path('product-list/', views.product_list, name='product-list'),
    path('product-list/manufacturer/<slug:manufacturer>/', views.manufacturer_specific, name='manufacturer-specific'),
    path('product-list/vehicle-brand/<slug:vehicle_brand>/', views.vehicle_brand_specific, name='vehicle-brand-specific'),
    path('product-list/scale/<slug:scale>/', views.scale_specific, name='scale-specific'),
    path('product-list/manufacturer/<slug:manufacturer>/<slug:slug>/', views.detail, name='detail'), 
    path('cart/', views.cart, name='cart'),
    path('cart/checkout/', views.checkout, name='checkout'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

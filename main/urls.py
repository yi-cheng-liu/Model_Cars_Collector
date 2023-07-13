from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import include
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('manufacturer-list/', views.manufacturer_list, name='manufacturer-list'),
    path('products/', views.products, name='products'),
    path('products/manufacturer/<slug:manufacturer>/', views.manufacturer_specific, name='manufacturer-specific'),
    path('products/vehicle-brand/<slug:vehicle_brand>/', views.vehicle_brand_specific, name='vehicle-brand-specific'),
    path('products/scale/<slug:scale>/', views.scale_specific, name='scale-specific'),
    path('products/manufacturer/<slug:manufacturer>/<slug:slug>/', views.detail, name='detail'), 
    path('delivery-and-returns/', views.delivery_and_returns, name='delivery-and-returns'),

    path('cart/', views.cart, name='cart'),
    path('cart/checkout/', views.checkout, name='checkout'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),

    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

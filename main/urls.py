from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('manufacturer-list/',views.manufacturer_list, name='manufacturer-list'),
    path('product-list/',views.product_list, name='product-list'),
    path('product-list/<slug:manufacturer>/<slug:slug>/', views.detail, name='detail'), 
    path('cart/',views.cart, name='cart'),
    path('cart/checkout/',views.checkout, name='checkout'),
    path('contact/',views.contact, name='contact'),
    path('about/',views.about, name='about'),
] 

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('product-list',views.product_list,name='product-list'),
    path('cart',views.cart,name='cart'),
    path('checkout',views.checkout,name='checkout'),
    path('contact',views.contact,name='contact'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('category-list',views.category_list,name='category-list'),
    path('brand-list',views.brand_list,name='brand-list'),
    path('cart',views.cart_list,name='cart'),
    path('product-list',views.product_list,name='product-list'),
]

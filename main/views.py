from django.shortcuts import render

from .models import Diecast
from .config import TOPBAR_1, TOPBAR_2, TOPBAR_3, TOPBAR_4, \
					EMAIL_ADDRESS, PHONE_NUMBER, LOCATION, \
					FACEBOOK_URL, GOOGLE_MAPS_URL, INSTAGRAM_URL

common_context = {
	'topbar_1': TOPBAR_1,
	'topbar_2': TOPBAR_2,
	'topbar_3': TOPBAR_3,
	'topbar_4': TOPBAR_4,
	'email': EMAIL_ADDRESS,
	'phone': PHONE_NUMBER,
	'location': LOCATION,
	'facebook': FACEBOOK_URL,
	'google_maps': GOOGLE_MAPS_URL,
	'instagram': INSTAGRAM_URL,
}

# Home Page
def home(request):
	context = common_context.copy()
	return render(request, 'index.html', context)

# Product List Page
def product_list(request):
	context = common_context.copy()
	diecasts = Diecast.objects.all()
	ctx = {'diecasts': diecasts, **context}
	return render(request,'product_list.html', ctx)

# Cart Page
def cart(request):
	context = common_context.copy()
	return render(request, 'cart.html', context)

# Checkout Page
def checkout(request):
	context = common_context.copy()
	return render(request, 'checkout.html', context)

# Contact Page
def contact(request):
	context = common_context.copy()
	return render(request, 'contact.html', context)
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator

from .models import Diecast, Manufacturer, VehicleBrand, Scale, CarouselItem
from .config import TOPBAR_1, \
					EMAIL_ADDRESS, PHONE_NUMBER, LOCATION, \
					FACEBOOK_URL, GOOGLE_MAPS_URL, INSTAGRAM_URL

common_context = {
	'topbar_1': TOPBAR_1,
	'email': EMAIL_ADDRESS,
	'phone': PHONE_NUMBER,
	'location': LOCATION,
	'facebook': FACEBOOK_URL,
	'google_maps': GOOGLE_MAPS_URL,
	'instagram': INSTAGRAM_URL,
}


# Home Page
def home(request):
	diecasts = Diecast.objects.all()
	carousel_items = CarouselItem.objects.all()
	vehicle_brands = VehicleBrand.objects.all()
	ctx = {'diecasts': diecasts, 'carousel_items' : carousel_items, 'vehicle_brands' : vehicle_brands, **common_context}
	return render(request, 'index.html', ctx)

# Manufacturer List Page
def manufacturer_list(request):
	manufacturers = Manufacturer.objects.all()
	ctx = {'manufacturers': manufacturers, **common_context}
	return render(request,'manufacturer_list.html', ctx)

# Manufacturer Specific Page
def manufacturer_specific(request, manufacturer):
	manufacturer_obj = get_object_or_404(Manufacturer, slug=manufacturer)
	diecasts = Diecast.objects.filter(manufacturer=manufacturer_obj)
	ctx = {'diecasts': diecasts, 'manufacturer': manufacturer_obj, **common_context}
	return render(request,'product_list.html', ctx)

# Vehicle Brand Specific Page
def vehicle_brand_specific(request, vehicle_brand):
	vehicle_brand_obj = get_object_or_404(VehicleBrand, slug=vehicle_brand)
	diecasts = Diecast.objects.filter(vehicle_brand=vehicle_brand_obj)
	ctx = {'diecasts': diecasts, 'vehicle_brand_obj': vehicle_brand_obj, **common_context}
	return render(request,'product_list.html', ctx)

# Scale Specific Page
def scale_specific(request, scale):
	scale_obj = get_object_or_404(Scale, slug=scale)
	diecasts = Diecast.objects.filter(scale=scale_obj)
	ctx = {'diecasts': diecasts, 'scale_obj': scale_obj, **common_context}
	return render(request,'product_list.html', ctx)

# Product List Page
def product_list(request):
	diecasts = Diecast.objects.all()
	manufacturers = Manufacturer.objects.all()
	vehicle_brands = VehicleBrand.objects.all()
	scales = Scale.objects.all()

	# Sort products
	sort = request.GET.get('sort')
	if sort == 'oldest':
		diecasts = diecasts.order_by('created_at')
	elif sort == 'latest':
		diecasts = diecasts.order_by('-created_at')
	elif sort == 'price_ascending':
		diecasts = diecasts.order_by('on_sale_price')
	elif sort == 'price_descending':
		diecasts = diecasts.order_by('-on_sale_price')
	elif sort == 'featured':
		diecasts = diecasts.filter(featured=True)
	elif sort == 'on_sale':
		diecasts == diecasts.filter(on_sale=True)
	else:
		diecasts = diecasts.order_by('-created_at')

	# Limit number of items
	limit = request.GET.get('limit')
	if limit:
		diecasts = diecasts[:int(limit)]
	else:
		limit = 20

	# Apply search query filter if it exists
	search_query = request.GET.get('search_query')
	if search_query:
		diecasts = diecasts.filter(title__icontains=search_query)

	# Pagination
	page_number = request.GET.get('page')
	paginator = Paginator(diecasts, limit)
	diecasts = paginator.get_page(page_number)

	ctx = {
        'diecasts': diecasts,
        'manufacturers': manufacturers,
		'vehicle_brands' : vehicle_brands,
        'scales': scales,
		'sort': sort,
        'limit': limit,
		'page_number': page_number,
        **common_context
    }
	return render(request,'product_list.html', ctx)

# Detail Page
def detail(request, manufacturer, slug):
	diecast = get_object_or_404(Diecast, manufacturer__slug=manufacturer, slug=slug)
	ctx = {'diecast': diecast, **common_context}
	return render(request, 'detail.html', ctx)

# Cart Page
def cart(request):
	ctx = {**common_context}
	return render(request, 'cart.html', ctx)

# Checkout Page
def checkout(request):
	ctx = {**common_context}
	return render(request, 'checkout.html', ctx)

# Contact Page
def contact(request):
	diecasts = Diecast.objects.all()	
	ctx = {'diecasts': diecasts, **common_context}
	return render(request, 'contact.html', ctx)

# About us Page
def about(request):
	vehicle_brands = VehicleBrand.objects.all()
	ctx = {'vehicle_brands': vehicle_brands, **common_context}
	return render(request, 'about.html', ctx)

from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.core.paginator import Paginator
from django.db.models import Count

from .models import Diecast, Manufacturer, VehicleBrand, Scale
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

def apply_search_filter(queryset, search_query):
    if search_query:
        queryset = queryset.filter(title__icontains=search_query)
    return queryset

# Home Page
def home(request):
	diecasts = Diecast.objects.all()

	# Apply search query filter if it exists
	search_query = request.GET.get('search_query')
	diecasts = apply_search_filter(diecasts, search_query)

	ctx = {'diecasts': diecasts, **common_context}
	return render(request, 'index.html', ctx)

# Manufacturer List Page
def manufacturer_list(request):
	manufacturers = Manufacturer.objects.all()
	ctx = {'manufacturers': manufacturers, **common_context}
	return render(request,'manufacturer_list.html', ctx)

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
	else:
		diecasts = diecasts.order_by('-created_at')

	featured = request.GET.get('featured')
	if featured == 'featured':
		diecasts = diecasts.filter(featured=True)
	elif featured == 'on_sale':
		diecasts == diecasts.filter(on_sale=True)
	elif featured == 'featured_on_sale':
		diecasts = diecasts.filter(featured=True, on_sale=True)
	else:
		diecasts = diecasts

	# Limit number of items
	limit = request.GET.get('limit')
	if limit:
		diecasts = diecasts[:int(limit)]
	else:
		limit = 20

	# Apply search query filter if it exists
	search_query = request.GET.get('search_query')
	diecasts = apply_search_filter(diecasts, search_query)

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

	# Apply search query filter if it exists
	diecasts = Diecast.objects.all()
	search_query = request.GET.get('search_query')
	diecasts = apply_search_filter(diecasts, search_query)

	ctx = {'diecasts' : diecasts, 'diecast': diecast, **common_context}
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

	# Apply search query filter if it exists
	search_query = request.GET.get('search_query')
	diecasts = apply_search_filter(diecasts, search_query)
	
	ctx = {'diecasts': diecasts, **common_context}
	return render(request, 'contact.html', ctx)

# About us Page
def about(request):
	vehicle_brands = VehicleBrand.objects.all()
	ctx = {'vehicle_brands': vehicle_brands, **common_context}
	return render(request, 'about.html', ctx)

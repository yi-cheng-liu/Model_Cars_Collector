from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.forms import UserCreationForm

from django.template.response import TemplateResponse
from payments import get_payment_model, RedirectNeeded

from .models import Diecast, Manufacturer, VehicleBrand, Scale, CarouselItem, AboutUs, DeliveryAndReturns
from .config import TOPBAR_1, \
					EMAIL_ADDRESS, PHONE_NUMBER, LOCATION, \
					FACEBOOK_URL, INSTAGRAM_URL, SHOPEE_URL, GOOGLE_MAPS_URL

common_context = {
	'topbar_1': TOPBAR_1,
	'email': EMAIL_ADDRESS,
	'phone': PHONE_NUMBER,
	'location': LOCATION,
	'facebook': FACEBOOK_URL,
	'instagram': INSTAGRAM_URL,
	'shopee': SHOPEE_URL,
	'google_maps': GOOGLE_MAPS_URL,
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
	return render(request,'products.html', ctx)

# Vehicle Brand Specific Page
def vehicle_brand_specific(request, vehicle_brand):
	vehicle_brand_obj = get_object_or_404(VehicleBrand, slug=vehicle_brand)
	diecasts = Diecast.objects.filter(vehicle_brand=vehicle_brand_obj)
	ctx = {'diecasts': diecasts, 'vehicle_brand': vehicle_brand_obj, **common_context}
	return render(request,'products.html', ctx)

# Scale Specific Page
def scale_specific(request, scale):
	scale_obj = get_object_or_404(Scale, slug=scale)
	diecasts = Diecast.objects.filter(scale=scale_obj)
	ctx = {'diecasts': diecasts, 'scale': scale_obj, **common_context}
	return render(request,'products.html', ctx)

# Product List Page
def products(request):
	diecasts = Diecast.objects.all()
	manufacturers = Manufacturer.objects.all()
	vehicle_brands = VehicleBrand.objects.all()
	scales = Scale.objects.all()
    
	total_diecasts = Diecast.objects.count()

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
		diecasts = diecasts.filter(on_sale=True)
	else:
		diecasts = diecasts.order_by('-created_at')

	# Limit number of items
	limit = request.GET.get('limit')
	if limit:
		diecasts = diecasts[:int(limit)]
	else:
		limit = 500

	# Apply search query filter if it exists
	search_query = request.GET.get('search_query')
	if search_query:
		diecasts = diecasts.filter(title__icontains=search_query)

	# Get page number from the GET request
	page = request.GET.get('page')

    # Create a Paginator object
	paginator = Paginator(diecasts, limit)  # Show 'limit' diecasts per page

	try:
		diecasts = paginator.page(page)
	except PageNotAnInteger:
        # If page is not an integer, deliver first page.
		diecasts = paginator.page(1)
	except EmptyPage:
        # If page is out of range (e.g., 9999), deliver last page of results.
		diecasts = paginator.page(paginator.num_pages)

	ctx = {
        'diecasts': diecasts,
        'manufacturers': manufacturers,
		'vehicle_brands' : vehicle_brands,
        'scales': scales,
        'total_diecasts' : total_diecasts,
		'sort': sort,
        'limit': limit,
		'page': page,
        **common_context
    }
	return render(request,'products.html', ctx)

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
def checkout(request, payment_id):
    payment = get_object_or_404(get_payment_model(), id=payment_id)

    try:
        form = payment.get_form(data=request.POST or None)
    except RedirectNeeded as redirect_to:
        return redirect(str(redirect_to))

    return TemplateResponse(
        request,
        'payment.html',
        {'form': form, 'payment': payment, **common_context}
    )

# Contact Page
def contact(request):
	ctx = {**common_context}
	return render(request, 'contact.html', ctx)

# About us Page
def about(request):
	about_us = AboutUs.objects.all()
	ctx = {'about_us': about_us, **common_context}
	return render(request, 'about.html', ctx)

# Delivery and Returns Page
def delivery_and_returns(request):
	delivery_and_returns = DeliveryAndReturns.objects.all()
	ctx = {'delivery_and_returns': delivery_and_returns, **common_context}
	return render(request, 'delivery_and_returns.html', ctx)

# Login Page
def login(request):

	ctx = {**common_context}
	return render(request, 'login.html', ctx)

# Register Page
def register(request):
	form = UserCreationForm()

	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
			form.save()

	ctx = {**common_context}
	return render(request, 'register.html', ctx)

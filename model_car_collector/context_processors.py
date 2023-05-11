from main.models import Manufacturer, VehicleBrand, Scale

def manufacturers(request):
    return {'manufacturers': Manufacturer.objects.all()}

def vehicle_brands(request):
    return {'vehicle_brands': VehicleBrand.objects.all()}

def scales(request):
    return {'scales': Scale.objects.all()}

from django.shortcuts import render
from .models import Location
from django.core.cache import cache
from .forms import LocationModelForm
# Create your views here.


def index(request):
    template = 'api/index.html'
    context={}
    context['name'] = 'Ashwani'
    location_form = LocationModelForm()
    context['location_form'] = location_form

    if(request.method == 'POST'):
        location_name = request.body.name
        print(location_name)
        context['location'] = get_geocoding("banglore")
        return render(request, template, context = context )
    else:
        context['name'] = 'Ashwani Get'

    return render(request, template, context=context)


def get_geocoding(location_name):
    location = Location()
    if is_location_in_cache(location_name):
        data = cache.__getattribute__(location_name)
        print("ashwani" + str(data))
        return data
    else:
        get_from_api(location_name)
        return

def is_location_in_cache(location_name):
    if cache.__contains__(location_name):
        return True
    return False

def get_from_api(location_name):
    location = Location()
    location.name = "random name api"
    location.lat = 0.0
    location.lon = 0.0
    return location
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
        # TODO: validate the form properly (LocationModelForm) instead of reading raw POST data.
        location_name = request.POST.get('name', 'bangalore')
        context['location'] = get_geocoding(location_name)
        return render(request, template, context = context )
    else:
        context['name'] = 'Ashwani Get'

    return render(request, template, context=context)


def get_geocoding(location_name):
    location = Location()
    if is_location_in_cache(location_name):
        return cache.get(location_name)
    else:
        location = get_from_api(location_name)
        cache.set(location_name, location)
        return location

def is_location_in_cache(location_name):
    return cache.get(location_name) is not None

def get_from_api(location_name):
    # TODO: call a real geocoding API. MOCK: returns a fixed placeholder location.
    location = Location()
    location.name = location_name
    location.lat = 0.0
    location.lon = 0.0
    return location
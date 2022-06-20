from __future__ import unicode_literals
from .models import Location ,SiteSetting, Provider, ProvidersCourse, FAQ

def country_locations(request):
    return {'country_locations': Location.objects.filter(location_type='Country', IsActive=1).values()}

def providers(request):
    return {'providers': Provider.objects.filter(IsActive=1).values()}

def providers_courses(request):
    return {'providers_courses': ProvidersCourse.objects.filter(IsActive=1).values()}

def faqs(request):
    return {'faqs': FAQ.objects.filter(IsActive=1).values()}

def settings(request):
    return {'settings': SiteSetting.load()}
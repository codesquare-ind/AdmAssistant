from datetime import datetime, timedelta
from django.contrib.sitemaps import Sitemap
from .models import Location, Provider
from django.urls import reverse
 
class StaticSitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.9
    protocol = 'https'

    def items(self):
        return ['home', ]

    def location(self, item):
        return reverse(item)


class LocationSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.9
    protocol = 'https'

    def items(self):
        return Location.objects.filter(location_type='Country', IsActive=1)

    def lastmod(self, obj):
        return datetime.today() + timedelta(-30)
        
    def location(self,obj):
        return '/%s' % (obj.slug)

class ProviderSitemap(Sitemap):
    changefreq = "weekly"
    priority = 1.0
    protocol = 'https'

    def items(self):
        return Provider.objects.filter(IsActive=1)

    def lastmod(self, obj):
        return obj.last_modified
        
    def location(self,obj):
        return '/providers/%s' % (obj.slug)
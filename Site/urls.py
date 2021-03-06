"""Site URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from django.conf import settings
from . import views
from .views import LocationDetailView, ProviderDetailView
from django.contrib.sitemaps.views import sitemap
from .sitemaps import *

#admin customization
admin.site.site_header="Admin Panel"
admin.site.site_title="Dashboard"
admin.site.index_title="My Admin Panel"

sitemaps = {
    'location':LocationSitemap,
    'provider':ProviderSitemap,
    'static':StaticSitemap
}

urlpatterns = [
    path('admin/', admin.site.urls),
    path('tinymce/', include('tinymce.urls')),
    path('', views.home, name='home'),
    path('<str:slug>/', LocationDetailView.as_view(), name='location'),
    path('providers/<str:slug>/', ProviderDetailView.as_view(), name='provider'),
    path('', include('Connect.urls')),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
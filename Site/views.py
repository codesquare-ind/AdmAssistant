from django.views.generic.detail import DetailView
from django.shortcuts import render
from django.conf import settings
from.models import Location, Provider, ProvidersCourse

def home(request):
        return render(request, 'home.html', context={})
        

class LocationDetailView(DetailView):
    # specify the model to use
    model = Location
    template_name = 'location_detail.html'
    slug_url_kwarg = 'slug'
    slug_field = 'slug'

    # override context data
    def get_context_data(self, *args, **kwargs):
        context = super(LocationDetailView,
             self).get_context_data(*args, **kwargs) 
        context['meta'] = {
                "title":"MBBS in "+self.object.full_name,
                "description":"MBBS in "+self.object.full_name +" is one of the best destination for indian Medical students. "+self.object.meta_description,
                "keywords" : ""+self.object.meta_keywords,
                "url" : self.object.slug,
                "author" : self.object.added_by
                }              
        return context

location_detail = LocationDetailView.as_view()

class ProviderDetailView(DetailView):
    # specify the model to use
    model = Provider
    template_name = 'provider_detail.html'
    slug_url_kwarg = 'slug'
    slug_field = 'slug'

    # override context data
    def get_context_data(self, *args, **kwargs):
        context = super(ProviderDetailView,
             self).get_context_data(*args, **kwargs) 
        context['meta'] = {
                "title":"MBBS from "+self.object.name,
                "description":"MBBS from "+self.object.name +" is really perfect for indian Medical students. "+self.object.short_description,
                "keywords" : "MBBS, NEET, JIPMER, MBBS from "+self.object.name+","+self.object.slug,
                "course" : ProvidersCourse.objects.filter(IsActive=1, provider_id=self.object.id, course_id=1)[0],
                "url" : self.object.slug,
                "author" : self.object.added_by
                }              
        return context

provider_detail = ProviderDetailView.as_view()